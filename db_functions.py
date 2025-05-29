import sqlite3
from contextlib import closing

DB_FILE = "chatbot.db"

def create_user(username, password_hash, email):
    try:
        with sqlite3.connect(DB_FILE) as conn:
            with closing(conn.cursor()) as cursor:
                cursor.execute(
                    "INSERT INTO Users (username, password_hash, email) VALUES (?, ?, ?)",
                    (username, password_hash, email)
                )
            conn.commit()
            return cursor.lastrowid
    except sqlite3.IntegrityError:
        return None

def assign_role(user_id, role_id):
    with sqlite3.connect(DB_FILE) as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute(
                "INSERT INTO UserRoles (user_id, role_id) VALUES (?, ?)",
                (user_id, role_id)
            )
        conn.commit()

def get_user_permissions(user_id):
    with sqlite3.connect(DB_FILE) as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute("""
                SELECT p.permission_name FROM Permissions p
                JOIN RolePermissions rp ON p.id = rp.permission_id
                JOIN UserRoles ur ON rp.role_id = ur.role_id
                WHERE ur.user_id = ?
            """, (user_id,))
            return [row[0] for row in cursor.fetchall()]
