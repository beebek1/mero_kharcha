import tkinter as tk
import sqlite3
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk
from threading import Thread

# Database Name
DB_NAME = "bisesh.db"

# Background color to match your app
BG_COLOR = "#b2b2a2"  # Changed to #b2b2a2
CHART_BG_COLOR = "#e6e6e6"
TITLE_COLOR = "#333333"
TEXT_COLOR = "#666666"
HIGHLIGHT_COLOR = "#ffcc00"

# Create tables if they don't exist and insert sample data if tables are empty
def user_base():
    conn = sqlite3.connect(DB_NAME)
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

    # Insert sample data if tables are empty
    cursor.execute("SELECT COUNT(*) FROM expense")
    if cursor.fetchone()[0] == 0:
        cursor.executemany("INSERT INTO expense (amount, category) VALUES (?, ?)", [
            (200, 'Food'),
            (150, 'Transport'),
            (100, 'Entertainment'),
            (250, 'Utilities'),
            (300, 'Home')
        ])

    cursor.execute("SELECT COUNT(*) FROM income")
    if cursor.fetchone()[0] == 0:
        cursor.executemany("INSERT INTO income (amount, category) VALUES (?, ?)", [
            (500, 'Salary'),
            (200, 'Freelance'),
            (100, 'Investments')
        ])

    conn.commit()
    conn.close()

# Fetch expense data from the database
def fetch_expense_data():
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT category, SUM(amount) FROM expense GROUP BY category")
        data = cursor.fetchall()
        conn.close()
        return data
    except Exception as e:
        print(f"Error fetching expense data: {e}")
        return []

# Fetch income data from the database
def fetch_income_data():
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT category, SUM(amount) FROM income GROUP BY category")
        data = cursor.fetchall()
        conn.close()
        return data
    except Exception as e:
        print(f"Error fetching income data: {e}")
        return []

# Function to generate a pie chart inside the Tkinter window
def generate_pie_chart(*args):
    chart_type = chart_option.get()  # Get the selected option

    # Clear previous content if it exists
    for widget in chart_list_frame.winfo_children():
        widget.destroy()

    # Fetch data based on selection
    if chart_type == "Expense":
        data = fetch_expense_data()
        title = "Expenses"
        colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']
    elif chart_type == "Income":
        data = fetch_income_data()
        title = "Income"
        colors = ['#2ecc71', '#f1c40f', '#e74c3c', '#3498db', '#9b59b6']
    else:
        return  # Do nothing if no valid option is selected

    # Debugging - Check if data exists
    if not data:  
        tk.Label(chart_list_frame, text="No data available!", font=("Arial", 14), fg="red", bg=CHART_BG_COLOR).pack()
        return
    
    # Extract categories and amounts
    categories = [row[0] for row in data]
    amounts = [row[1] for row in data]

    # Calculate percentages
    total = sum(amounts)
    percentages = [(amt / total) * 100 for amt in amounts]

    # Create a pie chart using Matplotlib
    fig, ax = plt.subplots(figsize=(5, 5))
    wedges, texts, autotexts = ax.pie(
        amounts, 
        labels=None,  
        autopct=lambda pct: f"{pct:.1f}%" if pct > 0 else "",  # Show percentage inside only
        startangle=140, 
        colors=colors,
        textprops={'fontsize': 12, 'weight': 'bold'}
    )

    # Adjust percentage text to be inside
    for autotext in autotexts:
        autotext.set_color("white")  # Set percentage text color
        autotext.set_fontsize(12)  # Set font size
        autotext.set_weight("bold")  # Set bold

    ax.set_title(title, fontsize=16, fontweight='bold', color=TITLE_COLOR)

    # Set background color to match the app
    fig.patch.set_facecolor(CHART_BG_COLOR)
    ax.set_facecolor(CHART_BG_COLOR)

    # Embed the pie chart into Tkinter
    canvas = FigureCanvasTkAgg(fig, master=chart_list_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

    # Add category details below with a line separator
    for i, (category, amount) in enumerate(zip(categories, amounts)):
        tk.Label(chart_list_frame, text=f"{category}  ----  ₹{amount:.2f}", 
                 font=("Arial", 12), fg=colors[i % len(colors)], bg=CHART_BG_COLOR).pack(anchor="w", padx=10)
        tk.Label(chart_list_frame, text="-" * 50, fg="black", bg=CHART_BG_COLOR).pack(anchor="w", padx=10)

# Function to run the database creation in a separate thread
def setup_database():
    user_base()

# Tkinter GUI
root = tk.Tk()
root.title("Mero Kharcha")  # Window title
root.geometry("600x800")  # Window size
root.configure(bg=BG_COLOR)  # Background color updated

# Fonts
title_font = ("Helvetica", 24, 'bold italic')
label_font = ("Helvetica", 12)
dropdown_font = ("Helvetica", 12)

# Labels
title_label = tk.Label(root, text="MERO KHARCHA", font=title_font, fg=HIGHLIGHT_COLOR, bg=BG_COLOR)
title_label.grid(row=0, column=0, pady=20, columnspan=2)

# Create a style for the dropdown
style = ttk.Style()
style.theme_use("clam")  # Use a modern theme
style.configure("TCombobox", 
                fieldbackground="#3a3a3a",  # Background color
                background="#3a3a3a",  # Dropdown background
                foreground="white",  # Text color
                borderwidth=2,
                relief="flat",
                font=("Helvetica", 12),
                padding=5)

style.map("TCombobox", 
          fieldbackground=[("readonly", "#3a3a3a")],  
          foreground=[("readonly", "white")],
          background=[("readonly", "#3a3a3a")])

# Updated Combobox with the new style
chart_option = tk.StringVar()
chart_option.set("Select Chart")  # Default value
chart_dropdown = ttk.Combobox(root, textvariable=chart_option, 
                              values=["Expense", "Income"], 
                              font=("Helvetica", 12), 
                              style="TCombobox", 
                              state="readonly")
chart_dropdown.grid(row=1, column=0, pady=10, padx=20)
chart_dropdown.bind("<<ComboboxSelected>>", generate_pie_chart)

# Frame to hold the pie chart and category list
chart_list_frame = tk.Frame(root, bg=CHART_BG_COLOR, bd=2, relief=tk.SUNKEN)
chart_list_frame.grid(row=2, column=0, padx=20, pady=20, sticky="nsew", columnspan=2)

# Configure grid weights for responsiveness
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(2, weight=1)

# Run database setup in a separate thread
thread = Thread(target=setup_database)
thread.start()

root.mainloop()