from tkinter import *
from tkinter import messagebox 
from PIL import ImageTk, Image

root = Tk()
root.title("Login Page")
root.geometry("925x500+300+200")
root.config(bg="#fff")
root.resizable(0, 0)

user_data = {
    "username": "admin",
    "password": "1234"  
}

# Predefined security answers
correct_answers = {
    "q1": "football",
    "q2": "msdhoni",
    "q3": "kathmandu"
}

def open_main_app():
    root.destroy() 
    app = Tk()
    app.title("App")
    app.geometry("925x500+300+200")
    app.config(bg="white")
    Label(app, text="Welcome!", bg='#fff', font=("Microsoft Yahei UI Light (Body)", 50, 'bold')).pack(expand=True)
    app.mainloop()

def signin():
    username = user.get()
    password = code.get()

    if username == user_data["username"] and password == user_data["password"]:
        open_main_app()
    else:
        messagebox.showerror("Invalid", "Incorrect username/password!\nPlease enter again.")

def forgot_password():
    fp_window = Toplevel(root)
    fp_window.title("Forgot Password")
    fp_window.geometry("400x350+500+250")
    fp_window.config(bg="#fff")

    Label(fp_window, text="Answer Security Questions", font=("Microsoft Yahei UI Light", 14, "bold"), bg="#fff").pack(pady=10)

    # Security Questions
    Label(fp_window, text="1. Which sport do you enjoy the most?",border=5, font=("Microsoft Yahei UI Light", 10,'bold'), bg="#fff").pack(pady=5)
    ans1_entry = Entry(fp_window, width=30)
    ans1_entry.pack(pady=5)

    Label(fp_window, text="2. Who is your favourite sportsperson?",border=5, font=("Microsoft Yahei UI Light", 10,'bold'), bg="#fff").pack(pady=5)
    ans2_entry = Entry(fp_window, width=30)
    ans2_entry.pack(pady=5)

    Label(fp_window, text="3. In which city were you born?",border=5, font=("Microsoft Yahei UI Light", 10,'bold'), bg="#fff").pack(pady=5)
    ans3_entry = Entry(fp_window, width=30)
    ans3_entry.pack(pady=5)

    def check_answers():
        ans1 = ans1_entry.get().strip().lower()
        ans2 = ans2_entry.get().strip().lower()
        ans3 = ans3_entry.get().strip().lower()

        if ans1 == correct_answers["q1"] and ans2 == correct_answers["q2"] and ans3 == correct_answers["q3"]:
            fp_window.destroy()  
            reset_password()  
        else:
            messagebox.showerror("Error", "Incorrect answers. Please try again.")

    Button(fp_window, text="Submit", width=15, pady=5, bg="#57a1f8", fg="white",
           border=0, command=check_answers).pack(pady=20)

def reset_password():
    reset_window = Toplevel(root)
    reset_window.title("Reset Password")
    reset_window.geometry("400x250+500+250")
    reset_window.config(bg="#fff")

    Label(reset_window, text="Enter New Password", font=("Microsoft Yahei UI Light", 14, "bold"), bg="#fff").pack(pady=10)

    new_pass_entry = Entry(reset_window, width=30, show="*")  
    new_pass_entry.pack(pady=5)

    def save_new_password():
        new_password = new_pass_entry.get().strip()

        if new_password:
            user_data["password"] = new_password  
            messagebox.showinfo("Success", "Your password has been reset successfully!")

            reset_window.destroy()  
            root.destroy()  
            open_main_app()  
        else:
            messagebox.showerror("Error", "Password cannot be empty!")

    Button(reset_window, text="Save", width=15, pady=5, bg="#57a1f8", fg="white",
           border=0, command=save_new_password).pack(pady=20)

# Load image
img = PhotoImage(file="login.png")
Label(root, image=img, bg="white").place(x=50, y=50)

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

heading = Label(frame, text="Sign in", fg="#57a1f8", bg="white", 
                font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=5)

def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, "Username")

user = Entry(frame, width=25, fg='black', border=0, bg='white', 
             font=('Microsoft YaHei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

def on_enter1(e):
    code.delete(0, 'end')

def on_leave1(e):
    name = code.get()
    if name == '':
        code.insert(0, "Password")

code = Entry(frame, width=25, fg='black', border=0, bg='white', 
             font=('Microsoft YaHei UI Light', 11))
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter1)
code.bind('<FocusOut>', on_leave1)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

Button(frame, width=39, pady=7, text="Sign in", bg="#57a1f8", fg='white', border=0,
       command=signin).place(x=35, y=204)

label = Label(frame, text="Don't have an account?", fg='black', bg='white',
              font=('Microsoft YaHei UI Light', 9))
label.place(x=75, y=270)

sign_up = Button(frame, width=6, text="Sign up", border=0, bg="white", cursor='hand2',
                 fg="#57a1f8")
sign_up.place(x=215, y=270)

forgot_btn = Button(frame, text="Forgot Password?", border=0, bg="white", cursor="hand2",
                    fg="#57a1f8", command=forgot_password)
forgot_btn.place(x=120, y=310)

root.mainloop()