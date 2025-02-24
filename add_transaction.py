from main_database import get_db_connection

def add_transaction(user_id, amount, category, notes, type, month_year, time, day):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''INSERT INTO transactions (user_id,amount, category, notes, type, month_year, time, day)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', (user_id, amount, category, notes, type, month_year, time, day))
    
    conn.commit()
    conn.close()
    # print(f"{type.capitalize()} added successfully!")

