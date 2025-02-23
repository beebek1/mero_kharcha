import sqlite3

DB_NAME = "user_database.db"  # Shared database file

def get_db_connection():
    """Establish and return a connection to the database."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # Enables dictionary-like row access
    return conn

def create_tables():
    """Create tables for users and transactions."""
    conn = get_db_connection()
    cursor = conn.cursor()

    # Users table (Username & Password can change, First & Last name unmutable)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    # Transactions table (Income & Expense)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            user_id INTEGER NOT NULL,
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            category TEXT NOT NULL, 
            notes TEXT,
            type TEXT NOT NULL CHECK(type IN ('income', 'expense')),
            month_year TEXT NOT NULL,
            time TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

# create_tables()

