from main_database import get_db_connection

def get_transactions(user_id,type=None):
    # global amount,transaction_list,total_expense,total_income
    conn = get_db_connection()
    cursor = conn.cursor()

    if type:
        cursor.execute(
            "SELECT amount, category, notes, type, month_year, time FROM transactions WHERE user_id = ? AND type = ?",
            (user_id, type)
        )
    else:
        cursor.execute(
            "SELECT amount, category, notes, type, month_year, time FROM transactions WHERE user_id = ?",
            (user_id,)
        )
    transactions = cursor.fetchall()
    conn.close()
    
        # Unpacking transactions into separate variables
    transaction_list = []
    for t in transactions:
        amount, category, notes, type, month_year, time = t  # Unpack tuple into variables
        transaction_dict = {
            "amount": float(amount),
            "category": category,
            "notes": notes,
            "type": type,
            "month_year": month_year,
            "time": time
        }
        transaction_list.append(transaction_dict)

    total_expense=0
    total_income=0
    for transactions in transaction_list:
        if transactions['type']=='expense':
            total_expense+=transactions['amount']
        else:
            total_income+=transactions['amount']

    final_amount=total_income-total_expense



    return transaction_list, total_expense, total_income, final_amount




