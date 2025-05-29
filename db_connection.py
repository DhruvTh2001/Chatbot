# database/db_connection.py

import sqlite3
from contextlib import contextmanager

DB_NAME = "chatbot.db"

@contextmanager
def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    try:
        yield conn
    finally:
        conn.close()

#this will make sure the database connection opens and closes safely every time you run a query 