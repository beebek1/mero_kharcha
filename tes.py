# import tkinter as tk
# from tkinter import ttk
# # Create main window
# root = tk.Tk()
# root.title("Transaction Table")

# #for fetching table in dashboard





# # Define columns (only the required fields)
# columns = ("Time", "Type", "Category", "Amount", "Notes")
# tree3 = ttk.Treeview(root, columns=columns, show="headings",height= 20)

# # Define column headings and width
# column_widths = {
#     "Time": 100,
#     "Type": 80,
#     "Category": 120,
#     "Amount": 100,
#     "Notes": 200
# }

# for col in columns:
#     tree3.heading(col, text=col)
#     tree3.column(col, width=column_widths[col], anchor="center")

# # Insert only the required fields into the table

# # Add Scrollbar
# scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree3.yview)
# tree3.configure(yscroll=scrollbar.set)

#     # Add proper suffix to the day (st, nd, rd, th)


# #to extract month and year and separate them
# for transaction in transaction_list:
#     # Extract month_year and time
#     month_n_year = transaction['month_year']  # e.g., 'February 2025'
#     time = int(transaction['day'])               # e.g., '11:37 AM'

#     month = month_n_year.split()[0]  # Get the first element (month)
#     # Add proper suffix to the day (st, nd, rd, th)
# if 11 <= time <= 13:
#     suffix = "th"
# else:
#     suffix = {1: "st", 2: "nd", 3: "rd"}.get(time % 10, "th")

# for transaction in transaction_list:
#     # Here, you can format the date or keep it as is
#     formatted_date = f"{time}{suffix} {month}"  # Use your previously defined format_date function
#     tree3.insert("", tk.END, values=(formatted_date, transaction["type"], transaction["category"], transaction["amount"], transaction["notes"]))

# # Pack widgets
# tree3.place(relx=0.01, rely=0.45, relwidth=0.98, relheight=0.45)












# # Run the Tkinter main loop
# root.mainloop()





        # for res in results:
        #     result_text += (f"ID: {res['id']} | Amount: {res['amount']} | "
        #                     f"Category: {res['category']} | Type: {res['type']} | "
        #                     f"Date: {res['date']} | Time: {res['time']}\n")






#delete transaction 



def delete_transaction(transaction_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    # Delete the transaction with the specified ID
    cursor.execute("DELETE FROM transactions WHERE id = ?", (transaction_id,))
    conn.commit()
    conn.close()
    print(f"Transaction {transaction_id} deleted successfully.")








#for unique notes if needed 

# def get_unique_notes(user_id):
#     """Fetch unique notes for a user from the transactions table."""
#     conn = get_db_connection()
#     cursor = conn.cursor()
    
#     cursor.execute(
#         "SELECT DISTINCT notes FROM transactions WHERE user_id = ?",
#         (user_id,)
#     )
    
#     notes = cursor.fetchall()
#     conn.close()

#     # Extracting notes from the fetched results
#     unique_notes=[]
#     for note in notes:
#         unique = note[0]
#         unique2=unique.lower()
#         unique_notes.append(unique2)
  
#    # Convert list of tuples to a list of strings
#     return unique_notes



# canvas_behind = tk.Canvas(root, width=400, height=300)
# canvas_behind.pack()

# # Draw a rectangle (x1, y1, x2, y2)
# canvas_behind.create_rectangle(50, 50, 250, 150, fill="lightblue", outline="black", width=2)