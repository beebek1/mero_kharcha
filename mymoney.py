import tkinter as tk
from adding_items import adding_data
from datetime import datetime
from fetch_transaction import get_transactions
from tkinter import ttk
from tkinter import messagebox
from main_database import delete_transaction

def create_main_window():
    root = tk.Tk()
    root.title("Dashboard") #added name to the window
    root.geometry("600x600")  # default window width and height
    root.configure(bg='white') #for background color

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
    
        #fonts and colors
    basic_font = ("Andale Mono",'10')
    topic_font = ("Zapfino", '14','bold')
    semi_topic_font=("DIN Alternate", '11','bold')
    specific_font=("DIN Alternate", '15','bold')

    BG_color='#FFFFFF'
    FG_color='black'

    Button_style = ttk.Style(root)

    Button_style.theme_use('clam')  # 'clam' is a more neutral theme

    Button_style.configure(
        "Flat.TButton",
        foreground="black",
        background="#EEF2F5",
        borderwidth=0,
        focusthickness=0,
        padding=(7,7),
        )
    Button_style.map(
        "Flat.TButton",
        background=[("active", "#B6BABE")],
        foreground=[("active", "white")]
        )

#for specific buttons
    Button_style_2 = ttk.Style(root)

    Button_style_2.theme_use('clam')  # 'clam' is a more neutral theme

    Button_style_2.configure(
        "Custom.TButton",
        foreground="white",
        background="#677D6A",
        borderwidth=0,
        focusthickness=0,
        padding=(7,7),
        font=semi_topic_font
        )
    Button_style_2.map(
        "Custom.TButton",
        background=[("active", "#1A3636")],
        foreground=[("active", "white")]
        )


    #for fetching table in dashboard
    style = ttk.Style(root)
    style.theme_use("clam")  # or another theme that allows styling

    # Configure Treeview style. 
    # "Treeview" controls the overall table appearance,
    style.configure("Treeview",
                    background="white",  # light grey background for rows F0F0F0
                    foreground="black",
                    fieldbackground="white"  # background color for cells
                    ) 
                    


    style.configure("Treeview.Heading",
                    background="white",  # dark color for headings
                    foreground="black",
                    font=("Arial",12, "bold"),
                    relief="flat")



    #for extra strip at top
    def create_top_layer(root):
        # Create a canvas
        canvas = tk.Canvas(root, width=600, height=77, bg="#A1A1A1", highlightthickness=0)
        canvas.place(x=0,y=0)  # Place the canvas at the bottom of the window

    create_top_layer(root)

    #for extra strip at bottom
    def create_bottom_layer(root):
        # Create a canvas
        canvas = tk.Canvas(root, width=600, height=100, bg="#DCD7C9", highlightthickness=0)
        canvas.place(x=0,y=540)  # Place the canvas at the bottom of the window

    create_bottom_layer(root)

    #create a canvas in the background

    canvas_behind = tk.Canvas(root, width=400, height=130,bg='#D0EFFF',highlightthickness=0)
    canvas_behind.place(relx=0.15, rely=0.2)

    #canvas for expense
    canvas_uphind_expense = tk.Canvas(root, width=100, height=55,bg='#FFCCCC',highlightthickness=0)
    canvas_uphind_expense.place(relx=0.60, rely=0.21)

    #canvas for income
    canvas_uphind_income = tk.Canvas(root, width=100, height=55,bg='#CCFFCC',highlightthickness=0)
    canvas_uphind_income.place(relx=0.60, rely=0.315)

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
        num_color='#006400'
    elif final_amount <0:
        num_color ='#C00000'
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
        if not search_query:
            messagebox.showinfo("Info", "Do a search") 
            tree_1_place()
            return
        

        else:
            results = []
            # Search for transactions that match the note (case-insensitive)
            for transaction in transaction_list:
                # Access values using dictionary keys
                transaction_id_search = transaction['id']
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
                            "id": transaction_id_search,
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
                tree.place_forget() 
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
                    transaction_id=transaction['id']
                    tree2.insert(
                        "", tk.END,text=transaction_id,
                        values=(final_2_dates[i], transaction["type"], transaction["category"], f"Rs. {transaction['amount']}", transaction["notes"])
                    )

                    # Pack widgets
                    tree2.place(relx=0.01, rely=0.45, relwidth=0.98, relheight=0.45)

            else:
                tree.place_forget() 
                messagebox.showinfo("Info", "No match found")  # Info popup

        
            def on_selection_search(event):
                """Show or hide the delete button based on selection."""
                selected_items = tree2.selection()
                if selected_items:
                    delete_button_search.place(relx=0.79, rely=0.84)
                    delete_button_search.lift() # Show button when a row is selected
                else:
                    delete_button_search.place_forget()  # Hide button if nothing is selected


            def delete_selected_search():
                """Delete the selected transaction from the Treeview and database."""
                selected_items_search = tree2.selection()  # Get selected row(s)
                for item in selected_items_search:
                    transaction_id = tree2.item(item, "text")  # Retrieve hidden transaction ID

                    # Confirm deletion with the user
                    confirm = messagebox.askyesno("Confirm Deletion", f"Delete this transaction?")
                    if confirm:
                        delete_transaction(transaction_id)  # Remove from database
                        tree2.delete(item)  # Remove from Treeview
                refresh(root)
            tree2.bind("<<TreeviewSelect>>", on_selection_search)

            delete_button_search= ttk.Button(root, text = 'Delete', command= delete_selected_search,style="Flat.TButton")


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
        transaction_id=(transaction['id'])
        tree.insert(
            "", tk.END,text=transaction_id,values=(final_2_dates[i], transaction["type"], transaction["category"], f"Rs. {transaction['amount']}", transaction["notes"])
        )
    #for regular table
    tree.place(relx=0.0001, rely=0.45, relwidth=1, relheight=0.45)

    # Pack widgets
    #after null search it will display previous data
    def tree_1_place():
        tree.place(relx=0.01, rely=0.45, relwidth=0.98, relheight=0.45)
        tree.lift()

    #for hiding delete button
    def on_selection(event):
        """Show or hide the delete button based on selection."""
        selected_items = tree.selection()
        if selected_items:
            delete_button.place(relx=0.79, rely=0.84)
            delete_button.lift() # Show button when a row is selected
        else:
            delete_button.place_forget()  # Hide button if nothing is selected


    #for deleting datas by using transaction id for tree
    def delete_selected():
        """Delete the selected transaction from the Treeview and database."""
        selected_items = tree.selection()  # Get selected row(s)
        for item in selected_items:
            transaction_id = tree.item(item, "text")  # Retrieve hidden transaction ID

            # Confirm deletion with the user
            confirm = messagebox.askyesno("Confirm Deletion", f"Delete this transaction?")
            if confirm:
                delete_transaction(transaction_id)  # Remove from database
                tree.delete(item)  # Remove from Treeview
        refresh(root)

    tree.bind("<<TreeviewSelect>>", on_selection)

    #labels for showing details
    # amount_label=tk.Label(root,text='Amount 💰',bg=BG_color,fg=FG_color )
    # Category_label=tk.Label(root,text='Category 📂',bg=BG_color,fg=FG_color )
    # type_label=tk.Label(root,text='Type 📝',bg=BG_color,fg=FG_color )
    # time_label=tk.Label(root,text='Time ⏳',bg=BG_color,fg=FG_color )
    # notes_label=tk.Label(root,text='Notes 🗒️',bg=BG_color,fg=FG_color )

    #texts
    mero_kharcha_label= tk.Label(root, text= "Mero Kharcha", font=topic_font ,fg=FG_color, bg="#A1A1A1")

    greeting_label= tk.Label(root, text= greeting, font=semi_topic_font, fg=FG_color, bg=BG_color)
    username_label= tk.Label(root, text= "BIBEK", font=semi_topic_font, fg=FG_color, bg=BG_color)

    rs_label= tk.Label(root, text= "Rs. ", font=specific_font, fg=FG_color, bg='#D0EFFF')
    final_amount_label= tk.Label(root, text= final_amount, font=specific_font, fg=num_color, bg='#D0EFFF')
    balance_label= tk.Label(root, text = 'Balance', font =basic_font, fg=FG_color,bg = '#D0EFFF')

    expense_label= tk.Label(root, text = 'EXPENSE', font =basic_font, fg=FG_color,bg = '#FFCCCC')
    total_expense_label= tk.Label(root, text= f'Rs. {total_expense}', font=semi_topic_font, fg='#8B0000', bg="#FFCCCC")

    income_label= tk.Label(root, text = 'INCOME', font =basic_font,fg=FG_color, bg = '#CCFFCC' )
    total_income_label= tk.Label(root, text=f'Rs. {total_income}', font=semi_topic_font, fg='#006400', bg="#CCFFCC")

    # Create an entry widget for note search
    search_entry = tk.Entry(root, font=("Arial", 14),width=9)

    # Create a search button
    search_button = ttk.Button(root, text="Search",command=search_note,style="Flat.TButton")



    #paddings
    #text's placements
    mero_kharcha_label.place(relx=0.02, rely=0.009) 

    greeting_label.place(relx=0.015, rely=0.13) 
    username_label.place(relx=0.015, rely=0.165)

    rs_label.place(x=110,y=150)
    final_amount_label.place(x=140,y=150)
    balance_label.place(x=110,y=180)

    expense_label.place(relx=0.61, rely=0.22) 
    total_expense_label.place(relx=0.61, rely=0.25) 

    income_label.place(relx=0.61, rely=0.325)  
    total_income_label.place(relx=0.61, rely=0.355) 

    search_button.place(relx=0.8, rely=0.0325)
    search_button.lift()

    search_entry.place(relx=0.6095, rely=0.03)
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
    adding_data_button= ttk.Button(root, text = 'Add', command= lambda : [root.destroy(), adding_data()],style="Custom.TButton")
    analysis_button= ttk.Button(root, text = 'Analysis', command= lambda : [root.destroy(), adding_data()], style="Custom.TButton" )
    set_budge_button= ttk.Button(root, text = 'Set Budget', command= lambda : [root.destroy(), adding_data()], style="Custom.TButton")
    Home_button= ttk.Button(root, text = 'Home', command= refresh,style="Custom.TButton")
    
    delete_button= ttk.Button(root, text = 'Delete', command= delete_selected,style="Flat.TButton")


    #button's placements
    Home_button.place(relx=0.03, rely=0.925) 
    adding_data_button.place(relx=0.29, rely=0.925)  #0.25
    analysis_button.place(relx=0.54, rely=0.925)
    set_budge_button.place(relx=0.79, rely=0.925)


    # delete_button.place_forget()

    # Bind event to detect selection changes
    root.mainloop()

def refresh(root):
    root.destroy()  # Close the current window
    create_main_window()  # Create a new instance of the main window

# Start the application
create_main_window()