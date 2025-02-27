import sqlite3

DB_NAME = "user_database.db"  # Shared database file

def get_db_connection():
    """Establish and return a connection to the SQLite database."""
    try:
        conn = sqlite3.connect(DB_NAME)  # Increase timeout if needed
        print("Database connection successful!")
        return conn  # Return the connection for further use
    except sqlite3.Error as e:
        print(f"Database connection failed: {e}")
        return None

def create_tables():
    """Create tables for users and transactions."""
    conn = get_db_connection()
    cursor = conn.cursor()

    # Users table (Username & Password can change, First & Last name unmutable)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE NOT NULL,
            email TEXT NOT NULL,
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
            time TEXT NOT NULL,
            day TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

#to delete a transaction
def delete_transaction(transaction_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    # Delete the transaction with the specified ID
    cursor.execute("DELETE FROM transactions WHERE id = ?", (transaction_id,))
    conn.commit()
    conn.close()
    print(f"Transaction {transaction_id} deleted successfully.")

