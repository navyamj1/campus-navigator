CREATE DATABASE campus_navigation1;

USE campus_navigation1;

CREATE TABLE location1 (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    type VARCHAR(255) NOT NULL,    
    latitude DOUBLE NOT NULL,
    longitude DOUBLE NOT NULL,
    location POINT NOT NULL,
    SPATIAL INDEX(location)
);

INSERT INTO location1 (name, type, latitude, longitude, location)
VALUES 
('CET Main Building', 'building', 8.5242, 76.9332, POINT(76.9332, 8.5242)),
('Library', 'building', 8.5262, 76.9345, POINT(76.9345, 8.5262)),
('Cafeteria', 'restaurant',8.545394135439452, 76.90462354028926, POINT(76.90462354028926,8.545394135439452)),
('Park', 'park', 8.5291, 76.9379, POINT(76.9379, 8.5291));

INSERT INTO location1 (name, type, latitude, longitude, location) 
VALUES ('Dhwani Stage','Open Air Theatre',8.545393233118125, 76.9041772374459,POINT(76.9041772374459,8.545393233118125));
UPDATE location1 
SET 
    name = 'Cafeteria', 
    type = 'restaurant', 
    latitude = 8.545394135439452, 
    longitude = 76.90462354028926, 
    location = POINT(76.90462354028926, 8.545394135439452)
WHERE id = 3;

UPDATE location1
SET 
    name = 'CET Main Building',
    latitude = 8.54607649683247,
    longitude = 76.90630808152046,
    location = POINT(76.90630808152046, 8.54607649683247)
WHERE id = 1;

UPDATE location1
SET 
    name = 'Library',
    latitude = 8.54559694242865,
    longitude = 76.90652473485099,
    location = POINT(76.90652473485099, 8.54559694242865)
WHERE id = 2;

UPDATE location1
SET 
    name = 'Gazebo',
    latitude = 8.545144902730996,
    longitude = 76.90450108526674,
    location = POINT(76.90450108526674, 8.545144902730996)
WHERE id = 4;
DELETE FROM location1 WHERE id IN (13,14,15,16);

SELECT * FROM location1;
CREATE TABLE programs (
    id INT AUTO_INCREMENT PRIMARY KEY,
	program VARCHAR(255) NOT NULL,
    time VARCHAR(255) NOT NULL,
    latitude DOUBLE NOT NULL,
    longitude DOUBLE NOT NULL,
    location POINT NOT NULL,
    SPATIAL INDEX(location)
);
SELECT * FROM programs;
ALTER TABLE programs ADD venue VARCHAR(255);
INSERT INTO programs (program, time, latitude, longitude, location,venue)
VALUES 
('Engineering Workshop', '10:00 AM - 12:00 PM', 8.54607649683247,76.90630808152046,POINT(76.90630808152046, 8.54607649683247),'CET Main Block'),
('LITSOC Informals', '2:00 PM - 4:00 PM', 8.545144902730996,76.90450108526674,POINT(76.90450108526674, 8.545144902730996),'Gazebo');
UPDATE programs SET venue='CET Main Building' WHERE id='1';
UPDATE programs SET venue='Gazebo' WHERE id='2';
INSERT INTO programs (program, time, venue, latitude, longitude, location)
VALUES 
('Book Club Meeting','11:00 AM -01:00 PM','Library', 8.54559694242865,76.90652473485099,POINT(76.90652473485099, 8.54559694242865));

INSERT INTO programs(program,time,venue,latitude,longitude,location)
VALUES
('Watch The Freakz Performance','05:30 PM-06:00 PM','Dhwani Stage',8.545393233118125, 76.9041772374459,POINT(76.9041772374459,8.545393233118125));
