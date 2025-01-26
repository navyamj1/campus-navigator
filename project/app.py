from flask import Flask,render_template, request, jsonify
import mysql.connector

app = Flask(__name__)

# Database configuration
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "Nayana@123",
    "database": "campus_navigation1"
}

# Fetch all locations
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/locations', methods=['GET'])
def get_locations():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        
        # Fetch all locations from the database
        cursor.execute("SELECT name AS place, latitude, longitude FROM location1")
        locations = cursor.fetchall()
        
        conn.close()
        return jsonify(locations)
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500

# Search for a specific location
@app.route('/search', methods=['GET'])
def search_location():
    query = request.args.get('q', '')  # Get the search query
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        
        # Search for locations by name
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
        cursor.execute("SELECT program, time, venue, latitude, longitude FROM programs")  # Adjust query if needed
        programs = cursor.fetchall()

        print("Programs fetched:", programs)  # Log the fetched programs for debugging

        conn.close()
        return jsonify(programs)
    except mysql.connector.Error as err:
        print("Error fetching programs:", err)  # Log any errors
        return jsonify({"error": str(err)}), 500

if __name__ == '__main__':
    app.run(debug=True)