import tkinter as tk
from adding_items import adding_data
from datetime import datetime
from fetch_transaction import get_transactions
from tkinter import font 
from tkinter import ttk
from tkinter import messagebox

root = tk.Tk()
root.title("Dashboard") #added name to the window
root.geometry("600x600")  # default window width and height
root.configure(bg='#5C7285') #for background color


#get data from database
transaction_list, total_expense, total_income, final_amount,notes=get_transactions(1)

#Toplevel for search button
def search_note():

    search= tk.Toplevel(root)
    search.geometry('300x300')
    search.title("Add data")
    search.configure(bg='white')

    search_query = entry.get().strip()  # Get the search input

    # Search for the note
    if search_query in notes:
        messagebox.showinfo("Search Result", f"'{search_query}' found!")
    else:
        messagebox.showinfo("Search Result", f"'{search_query}' not found.")

    search.mainloop()


# Create an entry widget for note search
entry = tk.Entry(root, font=("Arial", 14), width=30)
entry.place(x=350,y=80)

# Create a search button
search_button = tk.Button(root, text="Search", font=("Arial", 14), command=search_note)
search_button.place(x=440,y=80)


style = ttk.Style(root)
style.theme_use('alt')  # 'clam' is a more neutral theme
    
style.configure(
    "Flat.TButton",
    foreground="#112D4E",
    background="#A1E3F9",
    borderwidth=0,
    focusthickness=0,
    padding=(7,7),
    )
style.map(
    "Flat.TButton",
    background=[("active", "#A1E3F9")],
    foreground=[("active", "#112D4E")]
    )


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
day=now.strftime('%d')
current_time=now.strftime('%I:%M %p')
pm_am=now.strftime('%p')

#condition section

# Get the day of the week
day_of_week = now.strftime("%A")

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

month_label=tk.Label(root,text=f"{month},",bg=BG_color,fg=FG_color )
day_label=tk.Label(root,text=f'{day},',bg=BG_color,fg=FG_color )
year_label=tk.Label(root,text=year,bg=BG_color,fg=FG_color )
current_time_label=tk.Label(root, text=current_time,bg=BG_color,fg=FG_color)
day_of_week_label=tk.Label(root,text=day_of_week,bg=BG_color,fg=FG_color )

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

#for time and date
month_label.place(x=253,y=265)   #month_label.place(x=76,y=205)
day_label.place(x=70, y=330)
day_of_week_label.place(x=92, y=330)
year_label.place(x=313, y=265)

create_bottom_layer(root)


#buttons
adding_data_button= ttk.Button(root, text = 'Add', command= lambda : [root.destroy(), adding_data()],style="Flat.TButton")
analysis_button= ttk.Button(root, text = 'Analysis', command= lambda : [root.destroy(), adding_data()], style="Flat.TButton" )
categories_button= ttk.Button(root, text = 'Categories', command= lambda : [root.destroy(), adding_data()], style="Flat.TButton")

#button's placements
adding_data_button.place(x=40, y=555)
analysis_button.place(x=255, y=555)
categories_button.place(x=440, y=555)

print(notes)

root.mainloop()