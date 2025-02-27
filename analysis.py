import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk
from threading import Thread
from fetch_transaction import get_transactions



def get_analysis():
    # Tkinter GUI
    root = tk.Tk()
    root.title("Mero Kharcha")  # Window title
    root.geometry("600x600")  # Window size
    root.resizable
    root.configure(bg="white")  # Background color updated

    # Fonts
    title_font = ("Helvetica", 24, 'bold italic')
    label_font = ("Helvetica", 12)
    dropdown_font = ("Helvetica", 12)

    semi_topic_font=("DIN Alternate", '11','bold')

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


    #fetch data from database 
    unfiltered_expense_data=get_transactions(1,'expense')
    unfiltered_income_data=get_transactions(1,'income')

    # # Labels
    # title_label = tk.Label(root, text="MERO KHARCHA", font=title_font, fg=HIGHLIGHT_COLOR, bg=BG_COLOR)
    # title_label.grid(row=0, column=0, pady=20, columnspan=2)

    # Background color to match your app
    BG_COLOR = "#b2b2a2"  # Changed to #b2b2a2
    CHART_BG_COLOR = "#e6e6e6"
    TITLE_COLOR = "#333333"
    TEXT_COLOR = "#666666"
    HIGHLIGHT_COLOR = "#ffcc00"


    # Function to generate a pie chart inside the Tkinter window
    def generate_pie_chart(*args):
        chart_type = chart_option.get()  # Get the selected option

        # Clear previous content if it exists
        for widget in chart_list_frame.winfo_children():
            widget.destroy()

        # Fetch data based on selection
        if chart_type == "Expense":
            data = unfiltered_expense_data
            title = "Expenses"
            colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
        elif chart_type == "Income":
            data = unfiltered_income_data
            title = "Income"
            colors = ['#2ecc71', '#f1c40f', '#e74c3c', '#3498db']
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
        fig, ax = plt.subplots(figsize=(4, 4 ))
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
        canvas.get_tk_widget().place(x=0,y=10)

        # Add category details below with a line separator
        for i, (category, amount) in enumerate(zip(categories, amounts)):
            # Adjust rely value to prevent overlap

            # Category label
            tk.Label(chart_list_frame, text=f"{category}  ----  Rs.{amount:.2f}", 
                    font=("Arial", 12), fg=colors[i % len(colors)], bg=CHART_BG_COLOR).place(row=i, column=0,relx=0.54, rely=0.925)   #row=i, column=0, 

   #pack(anchor="e", padx=6)
            # Function to run the database creation in a separate thread

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
    chart_dropdown.grid(row=1, column=0, pady=10, padx=10)
    chart_dropdown.bind("<<ComboboxSelected>>", generate_pie_chart)

    # Frame to hold the pie chart and category list
    chart_list_frame = tk.Frame(root, bg=CHART_BG_COLOR, bd=2,height=300)
    chart_list_frame.grid(row=2, column=0, padx=0, pady=0, sticky="nsew")

    # Configure grid weights for responsiveness
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(2, weight=1)

    #buttons
    adding_data_button= ttk.Button(root, text = 'Add',style="Custom.TButton" )
    analysis_button= ttk.Button(root, text = 'Analysis', style="Custom.TButton" )
    set_budget_button= ttk.Button(root, text = 'Set Budget',style="Custom.TButton" )
    Home_button= ttk.Button(root, text = 'Home',style="Custom.TButton")   


    #button's placements
    Home_button.place(relx=0.03, rely=0.925) 
    adding_data_button.place(relx=0.29, rely=0.925) 
    analysis_button.place(relx=0.54, rely=0.925)
    set_budget_button.place(relx=0.79, rely=0.925)

    root.mainloop()

# get_analysis()