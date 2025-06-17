from flask import Flask,render_template, request, jsonify
import mysql.connector
import os

app = Flask(__name__)


db_config = {
    "host":os.environ["DB_HOST"],
    "user": os.environ["DB_USER"],
    "password": os.environ["DB_PASSWORD"],
    "database": os.environ["DB_NAME"],
    "port":int(os.environ.get("DB_PORT", 3306))
}


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/locations', methods=['GET'])
def get_locations():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        
        
        cursor.execute("SELECT name AS place, latitude, longitude FROM location1")
        locations = cursor.fetchall()
        
        conn.close()
        return jsonify(locations)
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500


@app.route('/search', methods=['GET'])
def search_location():
    query = request.args.get('q', '') 
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        

        cursor.execute(
            "SELECT name AS place, latitude, longitude FROM location1 WHERE name LIKE %s",
            (f"%{query}%",)
        )
        locations = cursor.fetchall()
        
        conn.close()
        return jsonify(locations)
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500
    
@app.route('/programs', methods=['GET'])
def get_programs():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT program, time, venue, latitude, longitude FROM programs")  
        programs = cursor.fetchall()

        print("Programs fetched:", programs)  

        conn.close()
        return jsonify(programs)
    except mysql.connector.Error as err:
        print("Error fetching programs:", err) 
        return jsonify({"error": str(err)}), 500

if __name__ == '__main__':
    app.run(debug=True)
