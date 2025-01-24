import mysql.connector

# Database connection details
db_config = {
    "host": "localhost",
    "user": "root",  # Replace with your MySQL username
    "password": "Mohithallu90@",  # Replace with your MySQL password
}

# SQL commands to create the schema
schema = """
CREATE DATABASE IF NOT EXISTS CollaborativeWikiPlatform;

USE CollaborativeWikiPlatform;

-- Users Table
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(150) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(128) NOT NULL,  -- Matches Django's default password hash length
    role ENUM('admin', 'editor', 'contributor') DEFAULT 'contributor',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Articles Table
CREATE TABLE IF NOT EXISTS articles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    author_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (author_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Comments Table
CREATE TABLE IF NOT EXISTS comments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    article_id INT NOT NULL,
    user_id INT NOT NULL,
    comment TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (article_id) REFERENCES articles(id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Article Version Control
CREATE TABLE IF NOT EXISTS article_versions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    article_id INT NOT NULL,
    content TEXT NOT NULL,
    version INT NOT NULL,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (article_id) REFERENCES articles(id) ON DELETE CASCADE
);
"""

try:
    # Connect to MySQL server
    connection = mysql.connector.connect(
        host=db_config["host"],
        user=db_config["user"],
        password=db_config["password"]
    )

    cursor = connection.cursor()

    # Execute schema creation
    for command in schema.split(";"):
        command = command.strip()
        if command:
            cursor.execute(command)
    
    connection.commit()
    print("Database and tables created successfully.")
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()
