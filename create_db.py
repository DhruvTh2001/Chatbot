import sqlite3
from contextlib import closing

# SQL commands to create tables if they don't exist already (for sign up)
schema = """
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS Roles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    role_name TEXT UNIQUE NOT NULL,
    description TEXT
);

CREATE TABLE IF NOT EXISTS UserRoles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    role_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(id),
    FOREIGN KEY (role_id) REFERENCES Roles(id)
);

CREATE TABLE IF NOT EXISTS Permissions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    permission_name TEXT UNIQUE NOT NULL,
    description TEXT
);

CREATE TABLE IF NOT EXISTS RolePermissions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    role_id INTEGER NOT NULL,
    permission_id INTEGER NOT NULL,
    FOREIGN KEY (role_id) REFERENCES Roles(id),
    FOREIGN KEY (permission_id) REFERENCES Permissions(id)
);
"""

# Function to create the database and tables
def create_database():
    try:
        # Connect to SQLite database (creates file if not exists)
        with sqlite3.connect("chatbot.db") as conn:
            # Create a cursor object to execute SQL commands
            with closing(conn.cursor()) as cursor:
                cursor.executescript(schema)  # Run all SQL commands at once
            conn.commit()  # Save the changes
            print("✅ Database and tables created successfully.")
    except Exception as e:
        print("❌ Error creating database:", e)

if __name__ == "__main__":
    create_database()  # Run this function when the script is executed
