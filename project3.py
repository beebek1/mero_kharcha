from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Budget Tracker")
root.geometry("925x500+300+200")
root.config(bg="#fff")
root.resizable(0, 0)

balance = 1000  # Example starting balance
expenses = []

def add_expense():
    global balance
    category = category_entry.get()
    amount = amount_entry.get()
    
    if not category or not amount:
        messagebox.showerror("Error", "Please enter both category and amount")
        return
    
    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Error", "Amount must be a number")
        return
    
    expenses.append((category, amount))
    balance_label.config(text=f"Balance: ${balance - sum(a for _, a in expenses)}")
    expense_list.insert(END, f"{category}: ${amount}")
    
    category_entry.delete(0, END)
    amount_entry.delete(0, END)

# Image (If needed, replace with your actual image file)
img = PhotoImage(file=r"money.png")
Label(root, image=img, bg="white").place(x=50, y=50)

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

heading = Label(frame, text="Budget Tracker", fg="#57a1f8", bg="white", font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=60, y=5)

def create_entry(parent, placeholder, y_pos):
    entry = Entry(parent, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
    entry.place(x=30, y=y_pos)
    entry.insert(0, placeholder)

    def on_enter(e):
        if entry.get() == placeholder:
            entry.delete(0, 'end')

    def on_leave(e):
        if not entry.get():
            entry.insert(0, placeholder)

    entry.bind('<FocusIn>', on_enter)
    entry.bind('<FocusOut>', on_leave)
    Frame(parent, width=295, height=2, bg='black').place(x=25, y=y_pos + 27)

    return entry

category_entry = create_entry(frame, "Category", 80)
amount_entry = create_entry(frame, "Amount", 140)

Button(frame, width=39, pady=7, text="Add Expense", bg="#57a1f8", fg='white', border=0, command=add_expense).place(x=35, y=200)

balance_label = Label(frame, text=f"Balance: ${balance}", fg='black', bg='white', font=('Microsoft YaHei UI Light', 11, 'bold'))
balance_label.place(x=100, y=250)

expense_list = Listbox(frame, width=40, height=6, border=0, bg='white', font=('Microsoft YaHei UI Light', 10))
expense_list.place(x=25, y=280)

root.mainloop()
