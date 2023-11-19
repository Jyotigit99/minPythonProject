from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('LoginPage')
root.geometry('925x500+300+200')
root.configure(bg='#fff')
root.resizable(False, False)


def signin():
    username = user.get()
    password = code.get()

    if username == 'admin' and password == '1234':
        root.destroy()
        import menuPage



    elif username != 'admin' and password != '1234':
        messagebox.showerror("Invalid", "Invalid username and password")
    elif username == "" and password == "":
        messagebox.showerror("Invalid", "Please enter username and password")
    elif username == " ":
        messagebox.showerror("Invalid", "Enter username")
    elif password != '1234':
        messagebox.showerror("Invalid", "Invalid  password")
    elif username != 'admin':
        messagebox.showerror("Invalid", "Invalid  username")


img = PhotoImage(file='D:\jyoti document scan\pyhtonprojectphoto\loginpageimg.png')
Label(root, image=img, bg='white').place(x=100, y=100)

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

heading = Label(frame, text='Sign in', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=5)


def on_enter(e):
    user.delete(0, 'end')


def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')


user = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)


def on_focus_in(event):
    password = event.widget
    if password.get() == 'Password':
        password.delete(0, 'end')
        password.config(show='*')


def on_focus_out(event):
    password = event.widget
    if password.get() == '':
        password.insert(0, 'Password')
        password.config(show='')


code = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
code.bind("<FocusIn>", on_focus_in)
code.bind("<FocusOut>", on_focus_out)
code.place(x=30, y=150)
code.insert(0, 'Password')

Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

######################################################################3

Button(frame, width=40, pady=5, text='Sign in', bg='#57a1f8', fg='white', border=0, command=signin).place(x=30, y=204)
#label = Label(frame, text="Don't have account ?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
#label.place(x=75, y=275)

#sign_up = Button(frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#57a1f8')
#sign_up.place(x=215, y=275)

root.mainloop()
