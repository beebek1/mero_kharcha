from main_database import get_db_connection
 
def get_transactions(user_id, type=None):
    """Fetch transactions for a user and return total income, expense, final amount, and unique notes."""
    conn = get_db_connection()
    cursor = conn.cursor()

    if type == 'income':
        cursor.execute("SELECT category, SUM(amount) FROM transactions WHERE user_id = ? AND type = 'income' GROUP BY category", (user_id,))

        transactions = cursor.fetchall()
        conn.close()
        return transactions
    
    elif type == 'expense':
        cursor.execute("SELECT category, SUM(amount) FROM transactions WHERE user_id = ? AND type = 'expense' GROUP BY category", (user_id,))
        
        transactions = cursor.fetchall()
        conn.close()
    
        return transactions  # Immediately return, skipping the rest of the code
    else:
        cursor.execute(
            "SELECT id, amount, category, notes, type, month_year, time, day FROM transactions WHERE user_id = ?",
            (user_id,)
        )
    
    transactions = cursor.fetchall()
    conn.close()

    transaction_list = []
    for t in transactions:
        transaction_id ,amount, category, notes, type, month_year, time, day = t
        transaction_dict=({
                "id":transaction_id,
                "amount": float(amount),
                "category": category,
                "notes": notes,
                "type": type,
                "month_year": month_year,
                "time": time,
                "day": day,
            })
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
    # unique_notes = get_unique_notes(user_id)
    
    return transaction_list, total_expense, total_income, final_amount







