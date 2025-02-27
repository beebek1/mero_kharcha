from tkinter import *
from tkinter import messagebox
from new_user import add_user
from new_user import check_user_credentials
from mymoney import create_main_window

def main_sign_in():
    # Initialize main window
    root = Tk()
    root.title("Login Page")
    root.config(bg="#fff")
    root.resizable(False, False)

    # Dynamically center the window
    window_width = 925
    window_height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    def signup():
        sign_window = Toplevel(root)
        sign_window.title("Sign Up")
        sign_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
        sign_window.resizable(False, False)
        sign_window.config(bg="white")

        # Using the same image as in the login page
        sign_window.img = PhotoImage(file="saving.png")  # Store image reference
        Label(sign_window, image=sign_window.img, bg="white").place(x=50, y=50)

        frame = Frame(sign_window, width=350, height=350, bg="white")
        frame.place(x=480, y=70)

        heading = Label(frame, text="Start Saving Up", fg="#57a1f8", bg="white", font=('Arial', 20, 'bold'))
        heading.place(x=60, y=5)

        def create_entry(parent, placeholder, y_pos):
            entry = Entry(parent, width=25, fg='black', border=0, bg='white', font=('Arial', 11))
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

        signup_user_raw = create_entry(frame, "Username", 80)
        signup_email_raw = create_entry(frame, "Email", 140)
        signup_pass_raw = create_entry(frame, "Password", 200)

    #label for returning to sign in window
        label2 = Label(sign_window, text="Already have an account?", fg='black', bg='white', font=('Arial', 9))
        label2.place(x=540, y=380)

        #button for returning to sign in window
        sign_in = Button(sign_window, width=6, text="Sign in", border=0, highlightbackground="white", cursor='hand2', fg="#57a1f8",command= lambda : [sign_window.destroy()], borderwidth= 0)  #remaining added command
        sign_in.place(x=700, y=378)

        def final_save_new_user():

            # Retrieve actual values from the entry fields
            username = signup_user_raw.get().strip()  # Use strip() to remove any extra spaces
            email = signup_email_raw.get().strip()
            password = signup_pass_raw.get().strip()

            # Pass the actual values to the add_user function
            a = add_user(username, email, password)

            if a == 0:
                messagebox.showinfo("error", "Account already Exists!")
                sign_window.destroy()
            else:
                messagebox.showinfo("Success", "Account created successfully!")
                sign_window.destroy()

        Button(frame, width=39, pady=7, text="Sign up", bg="#57a1f8", fg='white', border=0,
            command= final_save_new_user).place(x=35, y=260)
        
    # Login Page UI
    img = PhotoImage(file="login.png")
    Label(root, image=img, bg="white").place(x=50, y=50)

    frame = Frame(root, width=350, height=350, bg="white")
    frame.place(x=480, y=70)

    heading = Label(frame, text="Sign in", fg="#57a1f8", bg="white", font=('Arial', 20, 'bold'))
    heading.place(x=100, y=5)

    def create_input(parent, placeholder, y_pos, hide_text=False):
        entry = Entry(parent, width=25, fg='black', border=0, bg='white', font=('Arial', 11))
        entry.place(x=30, y=y_pos)
        entry.insert(0, placeholder)

        def on_enter(e):
            if entry.get() == placeholder:
                entry.delete(0, 'end')
                if hide_text:
                    entry.config(show="*")

        def on_leave(e):
            if not entry.get():
                entry.insert(0, placeholder)
                if hide_text:
                    entry.config(show="")

        entry.bind('<FocusIn>', on_enter)
        entry.bind('<FocusOut>', on_leave)
        Frame(parent, width=295, height=2, bg='black').place(x=25, y=y_pos + 27)

        return entry

    # Username Entry
    user = create_input(frame, "Username", 80)

    # Password Entry
    code = create_input(frame, "Password", 150, hide_text=True)

    #check credentials

    def signin_credentials_check():
        username = user.get()
        password = code.get()

        user_found= check_user_credentials(username, password)
        
        if user_found:
            root.destroy()  # Close the current window
            create_main_window() # Show success message if login is successful
        else:
            messagebox.showerror("Error", "Invalid Username or Password")  # Show error message if login fails

    # Sign in Button
    Button(frame, width=39, pady=7, text="Sign in", bg="#57a1f8", fg='white', border=0, command=signin_credentials_check).place(x=35, y=204)

    label = Label(frame, text="Don't have an account?", fg='black', bg='white', font=('Arial', 9))
    label.place(x=75, y=270)

    sign_up = Button(frame, width=6, text="Sign up", border=0, bg="white", cursor='hand2', fg="#57a1f8", command=signup )  #remaining added command
    sign_up.place(x=215, y=270)

    root.mainloop()
def to_open():
    main_sign_in()
main_sign_in()