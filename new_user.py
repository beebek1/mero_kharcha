import sqlite3
from main_database import get_db_connection
from tkinter import messagebox

# Function to add a user to the database
def add_user(username, email, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    a = 0
    
    try:
        cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
                       (username, email, password))
        conn.commit()
        print("User registered successfully!")
    except sqlite3.IntegrityError:
        return a 
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()


    # print(f"{type.capitalize()} added successfully!")

# Function to check user credentials
def check_user_credentials(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # Log the credentials being checked (avoid logging sensitive information in production)
        print(f"Checking credentials for username: {username}")

        # Fetch user data
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()  # Fetch the matching user
        
        if user:
            print("User found in the database.")
            return user  # Return user data if found
        else:
            print("No matching user found.")
            return None  # Return None if not found

    except Exception as e:
        print(f"An error occurred: {e}")  # Log the error message
        return None  # Return None on error

    finally:
        cursor.close()
        conn.close()

# Example usage
# if __name__ == "__main__":
#     # Adding a new user (replace with desired values)
#     add_user("new_user", "new_user@example.com", "secure_password")

# check_user_credentials('bibek1234','securepassword')

    # # Fetching user data
    # fetch_user_data()