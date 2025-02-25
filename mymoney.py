import tkinter as tk
from adding_items import adding_data
from datetime import datetime
from fetch_transaction import get_transactions
from tkinter import ttk
from tkinter import messagebox

root = tk.Tk()
root.title("Dashboard") #added name to the window
root.geometry("600x600")  # default window width and height
root.configure(bg='#5C7285') #for background color

#get data from database
transaction_list, total_expense, total_income, final_amount=get_transactions(1)

#abbreviate months name
def abbreviate_month(months):
    month_abbr = {
        "January": "Jan",
        "February": "Feb",
        "March": "Mar",
        "April": "Apr",
        "May": "May",
        "June": "Jun",
        "July": "Jul",
        "August": "Aug",
        "September": "Sep",
        "October": "Oct",
        "November": "Nov",
        "December": "Dec"
    }

    return month_abbr.get(month, month)

Button_style = ttk.Style(root)

Button_style.theme_use('alt')  # 'clam' is a more neutral theme

Button_style.configure(
    "Flat.TButton",
    foreground="#112D4E",
    background="#A1E3F9",
    borderwidth=0,
    focusthickness=0,
    padding=(7,7),
    )
Button_style.map(
    "Flat.TButton",
    background=[("active", "#A1E3F9")],
    foreground=[("active", "#112D4E")]
    )

#for fetching table in dashboard
style = ttk.Style(root)
style.theme_use("clam")  # or another theme that allows styling

# Configure Treeview style. 
# "Treeview" controls the overall table appearance,
style.configure("Treeview",
                background="#5C7285",  # light grey background for rows
                foreground="black",
                fieldbackground="#5C7285")  # background color for cells


style.configure("Treeview.Heading",
                background="#5C7285",  # dark color for headings
                foreground="white",
                font=("Arial", 12, "bold"))



#for extra strip at top
def create_top_layer(root):
    # Create a canvas
    canvas = tk.Canvas(root, width=600, height=77, bg="#27374D", highlightthickness=0)
    canvas.place(x=0,y=0)  # Place the canvas at the bottom of the window

create_top_layer(root)

#for extra strip at bottom
def create_bottom_layer(root):
    # Create a canvas
    canvas = tk.Canvas(root, width=600, height=100, bg="#3F4E4F", highlightthickness=0)
    canvas.place(x=0,y=540)  # Place the canvas at the bottom of the window

create_bottom_layer(root)

#fonts and colors
basic_font = ("Andale Mono",'10')
topic_font = ("Zapfino", '14','bold')
semi_topic_font=("DIN Alternate", '11','bold')

BG_color='#5C7285'
FG_color='black'
button_color="#3F72AF"

#Get current date and time
now = datetime.now()

#get month, year, day and time
month=now.strftime("%B")
year=now.strftime('%Y')
day_c=now.strftime('%d')
current_time=now.strftime('%I:%M %p')
pm_am=now.strftime('%p')

#condition section

# Get the day of the week
# day_of_week = now.strftime("%A")

if pm_am == "AM":
    greeting="Hi! GOOD MORNING"
else:
    greeting='Hi! GOOD AFTERNOON'

#condition for - red + green
if final_amount >0:
    num_color='light green'
elif final_amount <0:
    num_color ='#FF7F7F'
else:
    num_color ='black'

# #labels
# month_label=tk.Label(root,text=f"{month},",bg=BG_color,fg=FG_color )
# day_label=tk.Label(root,text=f'{day},',bg=BG_color,fg=FG_color )
# year_label=tk.Label(root,text=year,bg=BG_color,fg=FG_color )
# current_time_label=tk.Label(root, text=current_time,bg=BG_color,fg=FG_color)
# day_of_week_label=tk.Label(root,text=day_of_week,bg=BG_color,fg=FG_color )


#function to search items

def search_note():

    #make the previous table disappear
    tree.place_forget() 

    search_query = search_entry.get().strip()  # Get the search input
    results = []

    # Search for transactions that match the note (case-insensitive)
    for transaction in transaction_list:
        # Access values using dictionary keys
        transaction_id = transaction['id']
        amount = transaction['amount']
        category = transaction['category']
        notes = transaction['notes']
        type = transaction['type']
        month_year = transaction['month_year']
        time = transaction['time']
        day = transaction['day']
        notes_2=notes.strip()

        # Check if the search query is in the notes
        if search_query.lower() in notes_2.lower():
            try:
                # No need to convert amount, as it is already a float
                results_dict = {
                    "id": transaction_id,
                    "amount": amount,  # Keep it as a float
                    "category": category,
                    "notes": notes_2,
                    "type": type,
                    "month_year": month_year,
                    "time": time,
                    "day": day,
                }
                results.append(results_dict)  # Append the results

            except ValueError as e:
                print(f"Error processing transaction: {transaction}. Error: {e}")  # Log error

    # Format the results into a string for the label
    if results:

        # Define columns (only the required fields)
        columns = ("Time", "Type", "Category", "Amount", "Notes")
        tree2 = ttk.Treeview(root, columns=columns, show="headings",height= 20)

        # Define column headings and width
        column_widths = {
            "Time": 100,
            "Type": 80,
            "Category": 120,
            "Amount": 100,
            "Notes": 200
        }

        for col in columns:
            tree2.heading(col, text=col)
            tree2.column(col, width=column_widths[col], anchor="center")

        #to extract month and year and separate them
        final_dates = []  # Store formatted dates

        for transaction in results:
            month_n_year = transaction['month_year']  # e.g., 'February 2025'
            day = int(transaction['day'])  # Convert '24' to int

            month = month_n_year.split()[0]  # Extract month name
            abbreviated_month = abbreviate_month(month)  # Call function with correct argument

            # Determine the correct suffix
            if 11 <= day <= 13:
                suffix = "th"
            else:
                suffix = {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")

            formatted_date = f"{day}{suffix} {abbreviated_month}"
            final_dates.append(formatted_date)  # Store formatted date

            #to reverse the date so it matches the data

            final_2_dates=[]
        for i in range(len(final_dates)-1,-1,-1):

            a=final_dates[i]
            final_2_dates.append(a)

        # Insert into tree
        for i, transaction in enumerate(reversed(results)):
            tree2.insert(
                "", tk.END,
                values=(final_2_dates[i], transaction["type"], transaction["category"], f"Rs. {transaction['amount']}", transaction["notes"])
            )
            # Pack widgets
            tree2.place(relx=0.01, rely=0.45, relwidth=0.98, relheight=0.45)

    else:
        tree.place_forget()
        messagebox.showinfo("Info", f"No transactions found matching '{search_query}'")  # Info popup



            



 
# Define columns (only the required fields)
columns = ("Time", "Type", "Category", "Amount", "Notes")
tree = ttk.Treeview(root, columns=columns, show="headings",height= 20)

# Define column headings and width
column_widths = {
    "Time": 100,
    "Type": 80,
    "Category": 120,
    "Amount": 100,
    "Notes": 200
}

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=column_widths[col], anchor="center")

# Insert only the required fields into the table

# Add Scrollbar
scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
tree.configure(yscroll=scrollbar.set)



#to extract month and year and separate them
final_dates = []  # Store formatted dates

for transaction in transaction_list:
    month_n_year = transaction['month_year']  # e.g., 'February 2025'
    day = int(transaction['day'])  # Convert '24' to int


    month = month_n_year.split()[0]  # Extract month name
    abbreviated_month = abbreviate_month(month)  # Call function with correct argument

    # Determine the correct suffix
    if 11 <= day <= 13:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")

    formatted_date = f"{day}{suffix} {abbreviated_month}"
    final_dates.append(formatted_date)  # Store formatted date



        #to reverse the date so it matches the data

    final_2_dates=[]
    for i in range(len(final_dates)-1,-1,-1):

        a=final_dates[i]
        final_2_dates.append(a)


# Insert into tree
for i, transaction in enumerate (reversed(transaction_list)):
    tree.insert(
        "", tk.END,
        values=(final_2_dates[i], transaction["type"], transaction["category"], f"Rs. {transaction['amount']}", transaction["notes"])
    )
# Pack widgets
tree.place(relx=0.01, rely=0.45, relwidth=0.98, relheight=0.45)




#labels for showing details
# amount_label=tk.Label(root,text='Amount 💰',bg=BG_color,fg=FG_color )
# Category_label=tk.Label(root,text='Category 📂',bg=BG_color,fg=FG_color )
# type_label=tk.Label(root,text='Type 📝',bg=BG_color,fg=FG_color )
# time_label=tk.Label(root,text='Time ⏳',bg=BG_color,fg=FG_color )
# notes_label=tk.Label(root,text='Notes 🗒️',bg=BG_color,fg=FG_color )

#texts
mero_kharcha_label= tk.Label(root, text= "Mero Kharcha", font=topic_font ,fg=FG_color, bg="#27374D")

greeting_label= tk.Label(root, text= greeting, font=semi_topic_font, fg=FG_color, bg=BG_color)
username_label= tk.Label(root, text= "BIBEK", font=semi_topic_font, fg=FG_color, bg=BG_color)

rs_label= tk.Label(root, text= "Rs. ", font=semi_topic_font, fg=FG_color, bg=BG_color)
final_amount_label= tk.Label(root, text= final_amount, font=semi_topic_font, fg=num_color, bg=BG_color)
balance_label= tk.Label(root, text = 'Balance', font =basic_font, fg=FG_color,bg = BG_color)

expense_label= tk.Label(root, text = 'EXPENSE', font =basic_font, fg=FG_color,bg = BG_color)
total_expense_label= tk.Label(root, text= f'Rs. {total_expense}', font=semi_topic_font, fg='#FF7F7F', bg=BG_color)

income_label= tk.Label(root, text = 'INCOME', font =basic_font,fg=FG_color, bg = BG_color )
total_income_label= tk.Label(root, text=f'Rs. {total_income}', font=semi_topic_font, fg='light green', bg=BG_color)

# Create an entry widget for note search
search_entry = tk.Entry(root, font=("Arial", 14),width=8)

# Create a search button
search_button = tk.Button(root, text="Search", font=("Arial", 14),command=search_note)



#paddings
#text's placements
mero_kharcha_label.place(x=20, y=6)
greeting_label.place(x=50, y=80)
username_label.place(x=50,y=105)
rs_label.place(x=110,y=150)
final_amount_label.place(x=140,y=150)
balance_label.place(x=110,y=180)

expense_label.place(x=385, y=150)
total_expense_label.place(x=385, y=170)

income_label.place(x=385, y=210) 
total_income_label.place(x=385, y=230)

search_button.place(relx=0.8, rely=0.03)
search_button.lift()

search_entry.place(relx=0.63, rely=0.03)
search_entry.lift()


# #for time and date
# #month_label.place(x=253,y=265)   #month_label.place(x=76,y=205)
# day_label.place(x=70, y=330)
# day_of_week_label.place(x=92, y=330)
# #year_label.place(x=313, y=265)

#for previous results
# time_label.place(x=70,y=265)
# type_label.place(x=172,y=265)
# Category_label.place(x=274,y=265)
# amount_label.place(x=376,y=265)
# notes_label.place(x=480,y=265)





#buttons
adding_data_button= ttk.Button(root, text = 'Add', command= lambda : [root.destroy(), adding_data()],style="Flat.TButton")
analysis_button= ttk.Button(root, text = 'Analysis', command= lambda : [root.destroy(), adding_data()], style="Flat.TButton" )
categories_button= ttk.Button(root, text = 'Categories', command= lambda : [root.destroy(), adding_data()], style="Flat.TButton")


#button's placements
adding_data_button.place(x=40, y=555)
analysis_button.place(x=255, y=555)
categories_button.place(x=440, y=555)


root.mainloop()