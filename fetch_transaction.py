from main_database import get_db_connection

def get_unique_notes(user_id):
    """Fetch unique notes for a user from the transactions table."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        "SELECT DISTINCT notes FROM transactions WHERE user_id = ?",
        (user_id,)
    )
    
    notes = cursor.fetchall()
    conn.close()
    
    # Extracting notes from the fetched results
    unique_notes = [note[0] for note in notes]  # Convert list of tuples to a list of strings
    return unique_notes



def get_transactions(user_id, type=None):
    """Fetch transactions for a user and return total income, expense, final amount, and unique notes."""
    conn = get_db_connection()
    cursor = conn.cursor()

    if type:
        cursor.execute(
            "id, SELECT amount, category, notes, type, month_year, time FROM transactions WHERE user_id = ? AND type = ?",
            (user_id, type)
        )
    else:
        cursor.execute(
            "id, SELECT amount, category, notes, type, month_year, time FROM transactions WHERE user_id = ?",
            (user_id,)
        )
    
    transactions = cursor.fetchall()
    conn.close()
    
    transaction_list = []
    for t in transactions:
        transaction_id ,amount, category, notes, type, month_year, time = t
        transaction_dict = {
            "id":transaction_id,
            "amount": float(amount),
            "category": category,
            "notes": notes,
            "type": type,
            "month_year": month_year,
            "time": time
        }
        transaction_list.append(transaction_dict)

    total_expense = 0
    total_income = 0
    for transaction in transaction_list:
        if transaction['type'] == 'expense':
            total_expense += transaction['amount']
        else:
            total_income += transaction['amount']

    final_amount = total_income - total_expense
    
    # Fetch unique notes
    unique_notes = get_unique_notes(user_id)

    return transaction_id, total_expense, total_income, final_amount, unique_notes