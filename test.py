# import tkinter as tk

# def create_bottom_layer(root):
#     # Create a canvas
#     canvas = tk.Canvas(root, width=600, height=100, bg="lightgray", highlightthickness=0)
#     canvas.place(x=0,y=540)  # Place the canvas at the bottom of the window

#     # Optionally, you can draw shapes or other designs on the canvas
#     canvas.create_rectangle(0, 0, root.winfo_width(), 100, fill="lightgray", outline="")

# # Create the main application window
# root = tk.Tk()
# root.title("Layer Effect Example")
# root.geometry("600x600")

# # Create the bottom layer
# create_bottom_layer(root)
# text1=tk.Label(root,text="can you see me?")


# # Run the application
# root.mainloop()








from datetime import datetime

# Suppose you have a date string:
date_str = "2025-02-22"  # Format: YYYY-MM-DD

# Convert the string to a datetime object
date_obj = datetime.strptime(date_str, "%Y-%m-%d")

# Get the day of the week
day_of_week = date_obj.strftime("%A")
print(day_of_week)  # e.g., "Friday"