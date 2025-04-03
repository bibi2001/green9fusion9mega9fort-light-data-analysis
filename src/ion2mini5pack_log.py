# Development Log
# Started at 2025-04-03 08:50:15

# Added documentation

import sqlite3

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
        return None

def create_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT UNIQUE
            )
        ''')
        conn.commit()
    except sqlite3.Error as e:
        print(e)

# Update at 2025-04-04 03:48:06
# Added error handling
# This is a random comment
import re

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))

def extract_phone_numbers(text):
    pattern = r'\d{3}-\d{3}-\d{4}'
    return re.findall(pattern, text)