import tkinter as tk
from datetime import datetime
import subprocess
from tkinter import ttk , messagebox      #i removed sqlite3 
from add_transaction import add_transaction

#for adding data inside database
def adding_data():

    # Create the main window
    choosing_phase = tk.Tk()
    choosing_phase.title("Main Window")
    choosing_phase.geometry("600x600")
    choosing_phase.configure(bg="#F9F7F7")

    #fonts and colors
    basic_font = ("Arial MT",'10')
    topic_font = ("jokerman", '13','bold')
    BG_color='#5C7285'
    FG_color='black'
    button_color="#3F72AF"

    #categories
    expense_category= ['-category-','Food','Transport','Entertainment', 'Utilities', 'Home']
    income_category = ['-category-','Salary','Grants', 'Refunds', 'Lottery']

    style = ttk.Style(choosing_phase)
    style.theme_use('clam')  # 'clam' is a more neutral theme
    
    style.configure(
        "Flat.TButton",
        foreground="#112D4E",
        background="#A1E3F9",
        borderwidth=0,
        focusthickness=0,
        padding=(20,20),
        font=topic_font 
    )
    style.map(
        "Flat.TButton",
        background=[("active", "#A1E3F9")],
        foreground=[("active", "#112D4E")]
    )

        # Get current date and time
    now = datetime.now()

    #get month, year, day and time
    month=now.strftime("%B")
    year=now.strftime('%Y')
    day_c=now.strftime('%d')
    current_time=now.strftime('%I:%M %p')

    image=tk.PhotoImage(file='/Users/bibek/Desktop/new_python/Tkinter/crop image.png')
    bg_image_label = tk.Label(choosing_phase,image=image)

    def clear():
        # Function to validate inputs and clear entries
        amount = entry.get()
        category = selected_category.get()  # Get the selected category from the StringVar

                # Validate amount and category
        if not amount or category == expense_category[0] or category == income_category[0]:
            messagebox.showerror("Validation Error", "Amount and Category cannot be empty!")
            return # Exit the function if validation fails
        
        notes = note_entry.get("1.0", tk.END).strip()  # Get notes and strip whitespace
        month_year = f"{month} {year}"
        time = current_time # Get the current time
        day = day_c
        type = "expense" if category in expense_category else "income"  # Determine type based on category selection

         # Save the transaction to the database
        try:
            add_transaction(1, amount, category, notes, type, month_year, time, day)
            messagebox.showinfo("Success", "Transaction saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save transaction: {e}")
        finally:    
            # Clear entries if validation passes
            entry.delete(0, tk.END)  
            note_entry.delete("1.0", tk.END)
            selected_category.set(expense_category[0])  # Reset category to default
            return

#to return to main window
    def cancel_f():
        

        choosing_phase.destroy()  # Close the current window
        subprocess.Popen(["python3", "mymoney.py"])

    #functions for buttons
    def expense_f():
        global entry, note_entry, selected_category

        add_expense= tk.Toplevel(choosing_phase)
        add_expense.geometry('600x600')
        add_expense.title("Add data")
        add_expense.configure(bg='#5C7285')

        #black line 
        canvas = tk.Canvas(add_expense, width=2, height=20, highlightbackground=BG_color)   
    
        #labels
        amount_label =tk.Label(add_expense, text= "Amount :", font=basic_font,bg=BG_color,fg=FG_color)
        category_label=tk.Label(add_expense, text="Select Category :", font=basic_font,bg=BG_color,fg=FG_color)
        expense_label=tk.Label(add_expense,text="EXPENSE SECTION", font=topic_font,bg=BG_color,fg=FG_color)
        
        #entries
        entry=tk.Entry(add_expense, font=basic_font, width=9)   
        note_entry=tk.Text(add_expense, font=basic_font, width= 50, height= 10)

        #time and date 
        month_label=tk.Label(add_expense,text=month,bg=BG_color,fg=FG_color )
        day_label=tk.Label(add_expense,text=f'{day_c},',bg=BG_color,fg=FG_color )
        year_label=tk.Label(add_expense,text=year,bg=BG_color,fg=FG_color )
        current_time_label=tk.Label(add_expense, text=current_time,bg=BG_color,fg=FG_color)

        #select category
        selected_category = tk.StringVar(add_expense)
        selected_category.set(expense_category[0])

        # Create the OptionMenu widget
        category_menu_e = tk.OptionMenu(add_expense, selected_category, *expense_category)
        category_menu_e.config(font=basic_font,bg=BG_color,fg=FG_color)  

        #buttons for cancel and save
        cancel_button=tk.Button(add_expense,text='Cancel ✖', font=basic_font,highlightbackground= BG_color,command=cancel_f)
        save_button=tk.Button(add_expense,text='Save ✔',font=basic_font,highlightbackground=BG_color,command=clear)

        #paddings
        expense_label.place(x=225,y=80)
        amount_label.place(x=83, y=150)
        note_entry.place(x=75,y=230)
        entry.place(x=143, y=150)
        category_label.place(x=300, y=150)

        #for time and date
        month_label.place(x=76,y=205)
        day_label.place(x=135, y=205)
        year_label.place(x=156, y=205)
        current_time_label.place(x=206, y=205)

        canvas.place(x=196,y=205)

        category_menu_e.place(x=410,y=150)

        cancel_button.place(x=330,y=403)
        save_button.place(x=430,y=403)

    def income_f():
        global entry,note_entry,selected_category

        add_income= tk.Toplevel(choosing_phase)
        add_income.geometry('600x600')
        add_income.title("Add data")
        add_income.configure(bg='#5C7285')

        #black line 
        canvas = tk.Canvas(add_income, width=2, height=20, highlightbackground=BG_color)   

        #labels
        amount_label =tk.Label(add_income, text= "Amount :", font=basic_font,bg=BG_color,fg=FG_color)
        category_label=tk.Label(add_income, text="Select Category :", font=basic_font,bg=BG_color,fg=FG_color)
        income_label=tk.Label(add_income,text="INCOME SECTION", font=topic_font,bg=BG_color,fg=FG_color)
        
        #entries
        note_entry=tk.Text(add_income, font=basic_font, width= 50, height= 10)
        entry=tk.Entry(add_income, font=basic_font,width=9)

        #time and date 
        month_label=tk.Label(add_income,text=month,bg=BG_color,fg=FG_color )
        day_label=tk.Label(add_income,text=f'{day_c},',bg=BG_color,fg=FG_color )
        year_label=tk.Label(add_income,text=year,bg=BG_color,fg=FG_color )
        current_time_label=tk.Label(add_income, text=current_time,bg=BG_color,fg=FG_color)

        #select category
        selected_category=tk.StringVar(add_income)
        selected_category.set(income_category[0])

        #Create the OptionMenu widget
        category_menu_i=tk.OptionMenu(add_income,selected_category,*income_category)
        category_menu_i.config(font=basic_font,bg=BG_color,fg=FG_color)

        #buttons for cancel and save
        cancel_button=tk.Button(add_income,text='Cancel ✖', font=basic_font,highlightbackground= BG_color,command=cancel_f)
        save_button=tk.Button(add_income,text='Save ✔',font=basic_font,highlightbackground=BG_color,command=clear)

        #paddings
        income_label.place(x=225,y=80)
        amount_label.place(x=83,y=150)
        note_entry.place(x=75, y=230)
        entry.place(x=143, y=150)
        category_label.place(x=300, y=150)

        #for time and date
        month_label.place(x=76,y=205)
        day_label.place(x=135, y=205)
        year_label.place(x=156, y=205)
        current_time_label.place(x=206, y=205)

        canvas.place(x=196,y=205)

        category_menu_i.place(x=410,y=150)

        cancel_button.place(x=330,y=403)
        save_button.place(x=430,y=403)

    #Button in the main window to open the Toplevel window
    expense_button=ttk.Button(choosing_phase,text='Add Expense',style='Flat.TButton',command=expense_f)
    income_button=ttk.Button(choosing_phase,text='Add Income',style="Flat.TButton",command=income_f)

    #paddings
    income_button.place(x=218,y=200)
    expense_button.place(x=218,y=340)
    bg_image_label.pack()

    choosing_phase.mainloop()



