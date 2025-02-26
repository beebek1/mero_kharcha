from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Login Page")
root.geometry("925x500+300+200")
root.config(bg="#fff")
root.resizable(0, 0)

def signin():
    username = user.get()
    password = code.get()

    if username == "admin" and password == "1234":
        screen = Toplevel(root)
        screen.title("App")
        screen.geometry("925x500+300+200")
        screen.config(bg="white")

        Label(screen, text="Hello Everyone!", bg='#fff', font=("Calibri", 50, 'bold')).pack(expand=True)
    else:
        messagebox.showerror("Invalid", "Incorrect username or password!\nPlease try again.")

def signup():
    sign_window = Toplevel(root)
    sign_window.title("Sign Up")
    sign_window.geometry("925x500+300+200")
    sign_window.resizable(0,0)
    sign_window.config(bg="white")

    img = PhotoImage(file=r"saving.png")
    Label(sign_window, image=img, bg="white").place(x=50, y=50)
    sign_window.image = img

    frame = Frame(sign_window, width=350, height=350, bg="white")
    frame.place(x=480, y=70)

    heading = Label(frame, text="Start Saving Up", fg="#57a1f8", bg="white", font=('Microsoft YaHei UI Light', 23, 'bold'))
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

    signup_user = create_entry(frame, "Username", 80)
    signup_email = create_entry(frame, "Email", 140)
    signup_pass = create_entry(frame, "Password", 200)

    def check_signup():
        if not signup_user.get() or signup_user.get() == "Username" or \
           not signup_email.get() or signup_email.get() == "Email" or \
           not signup_pass.get() or signup_pass.get() == "Password":
            messagebox.showerror("Invalid Entry", "Invalid entry!") #changed error message
            return

        messagebox.showinfo("Success", "Account Created!")

    Button(frame, width=39, pady=7, text="Sign up", bg="#57a1f8", fg='white', border=0, command=check_signup).place(x=35, y=260)

img = PhotoImage(file="login.png")
Label(root, image=img, bg="white").place(x=50, y=50)

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

heading = Label(frame, text="Sign in", fg="#57a1f8", bg="white", font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=5)

def on_enter(e):
    if user.get() == "Username":
        user.delete(0, 'end')

def on_leave(e):
    if not user.get():
        user.insert(0, "Username")

user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

def on_enter1(e):
    if code.get() == "Password":
        code.delete(0, 'end')
        code.config(show="*")

def on_leave1(e):
    if not code.get():
        code.insert(0, "Password")
        code.config(show="")

code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter1)
code.bind('<FocusOut>', on_leave1)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

Button(frame, width=39, pady=7, text="Sign in", bg="#57a1f8", fg='white', border=0, command=signin).place(x=35, y=204)

label = Label(frame, text="Don't have an account?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
label.place(x=75, y=270)

sign_up = Button(frame, width=6, text="Sign up", border=0, bg="white", cursor='hand2', fg="#57a1f8", command=signup)
sign_up.place(x=215, y=270)

root.mainloop()