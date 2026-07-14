CREATE DATABASE IF NOT EXISTS opticrop;

USE opticrop;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fullname VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(15),
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE crop_predictions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_email VARCHAR(100),
    nitrogen FLOAT,
    phosphorus FLOAT,
    potassium FLOAT,
    temperature FLOAT,
    humidity FLOAT,
    ph FLOAT,
    rainfall FLOAT,
    predicted_crop VARCHAR(100),
    prediction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE fertilizer_predictions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_email VARCHAR(100),
    crop_name VARCHAR(100),
    fertilizer_name VARCHAR(100),
    prediction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE irrigation_predictions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_email VARCHAR(100),
    soil_moisture FLOAT,
    temperature FLOAT,
    rainfall FLOAT,
    recommendation VARCHAR(100),
    prediction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);