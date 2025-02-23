import sqlite3
from main_database import get_db_connection

def add_user(first_name, last_name, username, password):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO users (first_name, last_name, username, password) VALUES (?, ?, ?, ?)",
                       (first_name, last_name, username, password))
        conn.commit()
        print("User registered successfully!")
    except sqlite3.IntegrityError:
        print("Error: Username already exists!")
    
    conn.close()

# Example usage
add_user("Bibek", "Soti", "bibek123", "securepassword")