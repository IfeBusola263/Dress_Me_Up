-- Create the database
CREATE DATABASE IF NOT EXISTS dress_me_up_dev_db;

-- Use the database
USE dress_me_up_dev_db;

-- Create Events table
CREATE TABLE IF NOT EXISTS events (
    event_id VARCHAR(60) PRIMARY KEY,
    name VARCHAR(128) NOT NULL
);

-- Create Dresses table
CREATE TABLE IF NOT EXISTS dresses (
    id VARCHAR(60) PRIMARY KEY,
    name VARCHAR(128) NOT NULL,
    description VARCHAR(128) NOT NULL,
    brand VARCHAR(128) NOT NULL,
    category VARCHAR(128) NOT NULL,
    image VARCHAR(128) NOT NULL,
    event_id VARCHAR(60) NOT NULL,
    FOREIGN KEY (event_id) REFERENCES events(event_id)
);

-- Create Hair Style table
CREATE TABLE IF NOT EXISTS hair_style (
    id VARCHAR(60) PRIMARY KEY,
    name VARCHAR(128) NOT NULL,
    description VARCHAR(128) NOT NULL,
    length INTEGER NOT NULL,
    image VARCHAR(128) NOT NULL
);

-- Create Users table
CREATE TABLE IF NOT EXISTS users (
    id VARCHAR(60) PRIMARY KEY,
    name VARCHAR(60) NOT NULL,
    email VARCHAR(120) NOT NULL,
    profile_picture VARCHAR(60),
    preference VARCHAR(120),
    measurement VARCHAR(60) NOT NULL,
    outfits VARCHAR(60) NOT NULL,
    country VARCHAR(60) NOT NULL,
    state VARCHAR(60) NOT NULL,
    password VARCHAR(120) NOT NULL
);

-- Create Makeup Styles table
CREATE TABLE IF NOT EXISTS makeup_styles (
    id VARCHAR(60) PRIMARY KEY,
    name VARCHAR(120) NOT NULL,
    description VARCHAR(120) NOT NULL,
    makeup_type VARCHAR(60) NOT NULL,
    image VARCHAR(60) NOT NULL
);


-- Insert 5 instances into the Events table
INSERT INTO events (event_id, name)
VALUES
    ('919be9d0-5789-4b56-b785-0e4d72ecc8ba', 'Event 1 Name'),
    ('4703b2d8-e417-4243-a6f3-044fc06f020e', 'Event 2 Name'),
    ('919be9d0-5789-4b56-boi5-0e4d72ecc8ba', 'Event 3 Name'),
    ('478d6061-fc78-40c3-a1b2-0e906fb86da8', 'Event 4 Name'),
    ('48a5d328-3905-4cb5-b634-ddce3f593390', 'Event 5 Name');

-- Insert sample data into Dresses table
INSERT INTO dresses (id, name, description, brand, category, image, event_id)
VALUES
    ('017ec502-e84a-4a0f-92d6-d97e27bb6bdf', 'Dress 1', 'Description 1', 'Brand 1', 'Category 1', 'Image 1', '919be9d0-5789-4b56-b785-0e4d72ecc8ba'),
    ('05b0b99c-f10e-4e3a-88d1-b3187d6998ee', 'Dress 2', 'Description 2', 'Brand 2', 'Category 2', 'Image 2', '4703b2d8-e417-4243-a6f3-044fc06f020e'),
    ('9799648d-88dc-4e63-b858-32e6531bec5c', 'Dress 3', 'Description 3', 'Brand 3', 'Category 3', 'Image 3', '919be9d0-5789-4b56-b785-0e4d72ecc8ba'),
    ('1721b75c-e0b2-46ae-8dd2-f86b62fb46e6', 'Dress 4', 'Description 4', 'Brand 4', 'Category 4', 'Image 4', '478d6061-fc78-40c3-a1b2-0e906fb86da8'),
    ('d2398800-dd87-482b-be21-50a3063858ad', 'Dress 5', 'Description 5', 'Brand 5', 'Category 5', 'Image 5', '48a5d328-3905-4cb5-b634-ddce3f593390');

-- Insert sample data into Hair Style table
INSERT INTO hair_style (id, name, description, length, image)
VALUES
    ('1721b75c-e0b2-46ae-8dd2-f86b62fb46e6', 'Hair Style 1', 'Description 1', 20, 'Image 1'),
    ('02d9a2b5-7dca-423f-8406-707bc76abf7e', 'Hair Style 2', 'Description 2', 25, 'Image 2'),
    ('017ec502-e84a-4a0f-92d6-d97e27bb6bdf', 'Hair Style 3', 'Description 3', 30, 'Image 3'),
    ('073084e1-1d9d-49e6-8383-42ef6f4325b5', 'Hair Style 4', 'Description 4', 35, 'Image 4'),
    ('937ec502-e84a-4a0f-92d6-d97e27bb6bdf', 'Hair Style 5', 'Description 5', 40, 'Image 5');

-- Insert sample data into Users table
INSERT INTO users (id, name, email, profile_picture, preference, measurement, outfits, country, state, password)
VALUES
    ('d590593b-c4ef-4a9a-b631-9f4bf7a3d6c2', 'User 1', 'user1@example.com', 'Profile 1', 'Preference 1', 'Measurement 1', 'Outfits 1', 'Country 1', 'State 1', 'Password 1'),
    ('df2548db-377d-422e-b805-4e8e0c794302', 'User 2', 'user2@example.com', 'Profile 2', 'Preference 2', 'Measurement 2', 'Outfits 2', 'Country 2', 'State 2', 'Password 2'),
    ('017ec502-e84a-4a0f-92d6-d97e27bb6bdf', 'User 3', 'user3@example.com', 'Profile 3', 'Preference 3', 'Measurement 3', 'Outfits 3', 'Country 3', 'State 3', 'Password 3'),
    ('32945f6e-5a96-4233-b8ae-048d51323d7b', 'User 4', 'user4@example.com', 'Profile 4', 'Preference 4', 'Measurement 4', 'Outfits 4', 'Country 4', 'State 4', 'Password 4'),
    ('e6c33577-5de3-4481-9147-47ef4710b986', 'User 5', 'user5@example.com', 'Profile 5', 'Preference 5', 'Measurement 5', 'Outfits 5', 'Country 5', 'State 5', 'Password 5');

-- Insert sample data into Makeup Styles table
INSERT INTO makeup_styles (id, name, description, makeup_type, image)
VALUES
    ('989be9d0-5789-4b56-b785-0e4d72ecc8ba', 'Makeup Style 1', 'Description 1', 'Type 1', 'Image 1'),
    ('1ff1963c-7afa-470c-bc05-562b01549b09', 'Makeup Style 2', 'Description 2', 'Type 2', 'Image 2'),
    ('919be9d0-5789-4b56-b785-0e4d72ecc8ba', 'Makeup Style 3', 'Description 3', 'Type 3', 'Image 3'),
    ('19ae5055-f503-499d-a64f-2bf7d92eff5b', 'Makeup Style 4', 'Description 4', 'Type 4', 'Image 4'),
    ('899be9d0-5789-4b56-b785-0e4d72ecc8ba', 'Makeup Style 5', 'Description 5', 'Type 5', 'Image 5');


