import tkinter as tk
import sqlite3
import matplotlib.pyplot as plt

# Create tables if they don't exist
def user_base():
    conn = sqlite3.connect("income.db")
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS expense (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        amount REAL NOT NULL,
                        category TEXT NOT NULL
                      )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS income (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        amount REAL NOT NULL,
                        category TEXT NOT NULL
                      )''')

    conn.commit()
    conn.close()


# Insert expense data into the database
def insert_expense_data(amount, category):
    conn = sqlite3.connect("income.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO expense (amount, category) VALUES (?, ?)", 
                   (amount, category))
    conn.commit()
    conn.close()

# Insert income data into the database
def insert_income_data(amount, category):
    conn = sqlite3.connect("income.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO income (amount, category) VALUES (?, ?)", 
                   (amount, category))
    conn.commit()
    conn.close()

# Fetch expense data from the database
def fetch_expense_data():
    conn = sqlite3.connect("income.db")
    cursor = conn.cursor()
    cursor.execute("SELECT category, SUM(amount) FROM expense GROUP BY category")
    data = cursor.fetchall()
    conn.close()
    return data

# Fetch income data from the database
def fetch_income_data():
    conn = sqlite3.connect("income.db")
    cursor = conn.cursor()
    cursor.execute("SELECT category, SUM(amount) FROM income GROUP BY category")
    data = cursor.fetchall()
    conn.close()
    return data

def generate_pie_chart(chart_type):
    # Fetch data from the database based on the chart type
    if chart_type == "Expense":
        data = fetch_expense_data()
        title = "Expense Distribution by Category"
        colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']
    elif chart_type == "Income":
        data = fetch_income_data()
        title = "Income Distribution by Category"
        colors = ['#f1c40f', '#e74c3c', '#2ecc71', '#3498db', '#9b59b6']
    
    # Extract categories and amounts
    categories = [row[0] for row in data]
    amounts = [row[1] for row in data]
    
    # Create pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=140, colors=colors)
    plt.title(title)
    plt.show()
