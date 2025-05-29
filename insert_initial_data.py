import sqlite3
from contextlib import closing

# Function to insert initial users, roles, and permissions data
def insert_initial_data():
    # Lists of data to insert into tables
    users = [
        ('admin', 'hashed_password_1', 'admin@example.com'),
        ('editor', 'hashed_password_2', 'editor@example.com'),
        ('viewer', 'hashed_password_3', 'viewer@example.com'),
    ]
    roles = [
        ('Admin', 'Full access to all system functions'),
        ('Editor', 'Can modify content but limited admin rights'),
        ('Viewer', 'Can only view content'),
    ]
    user_roles = [
        (1, 1),  # Assign Admin role to user with id 1
        (2, 2),  # Assign Editor role to user with id 2
        (3, 3),  # Assign Viewer role to user with id 3
    ]
    permissions = [
        ('Read', 'Can read content'),
        ('Write', 'Can modify content'),
        ('Delete', 'Can delete content'),
    ]
    role_permissions = [
        (1, 1),  # Admin role has Read permission
        (1, 2),  # Admin role has Write permission
        (1, 3),  # Admin role has Delete permission
        (2, 1),  # Editor role has Read permission
        (2, 2),  # Editor role has Write permission
        (3, 1),  # Viewer role has Read permission
    ]

    try:
        with sqlite3.connect("chatbot.db") as conn:
            with closing(conn.cursor()) as cursor:
                # Insert data into tables, ignoring duplicates
                cursor.executemany("INSERT OR IGNORE INTO Users (username, password_hash, email) VALUES (?, ?, ?)", users)
                cursor.executemany("INSERT OR IGNORE INTO Roles (role_name, description) VALUES (?, ?)", roles)
                cursor.executemany("INSERT OR IGNORE INTO UserRoles (user_id, role_id) VALUES (?, ?)", user_roles)
                cursor.executemany("INSERT OR IGNORE INTO Permissions (permission_name, description) VALUES (?, ?)", permissions)
                cursor.executemany("INSERT OR IGNORE INTO RolePermissions (role_id, permission_id) VALUES (?, ?)", role_permissions)
            conn.commit()  # Save all changes
            print("✅ Initial data inserted successfully.")
    except Exception as e:
        print("❌ Error inserting initial data:", e)

if __name__ == "__main__":
    insert_initial_data()  # Run this when the script is executed
