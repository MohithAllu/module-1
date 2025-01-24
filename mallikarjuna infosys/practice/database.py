import mysql.connector

# Database connection details
db_config = {
    "host": "localhost",
    "user": "root",  # Replace with your MySQL username
    "password": "Mohithall90@",  # Replace with your MySQL password
}

# SQL commands to create the schema
schema = """
CREATE DATABASE CollaborativeWikiPlatform;

USE CollaborativeWikiPlatform;

-- Users Table
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    role ENUM('admin', 'editor', 'contributor') DEFAULT 'contributor',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Articles Table
CREATE TABLE articles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    author_id INT NOT NULL,
    status ENUM('draft', 'pending_approval', 'published') DEFAULT 'draft',
    version INT DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (author_id) REFERENCES users(id)
);

-- Comments Table
CREATE TABLE comments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    article_id INT NOT NULL,
    user_id INT NOT NULL,
    comment TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (article_id) REFERENCES articles(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Article Version Control
CREATE TABLE article_versions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    article_id INT NOT NULL,
    content TEXT NOT NULL,
    version INT NOT NULL,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (article_id) REFERENCES articles(id)
);
"""

try:
    # Connect to MySQL server
    connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mohithallu90@"  # Replace with your root password
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
