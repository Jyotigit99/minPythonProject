import tkinter as tk
from tkinter import *
from tkinter import messagebox

root =Tk()
root.title('Menu Page')
root.geometry('925x500+300+200')

root.configure(bg='#57a1f8')
root.resizable(False, False)

img = PhotoImage(file='D:\jyoti document scan\pyhtonprojectphoto\menuPage1.png')

Label(root, image=img, bg='white').place(x=330, y=130)


def signout():
    root.destroy()
    import loginPage



def our_command():


    import registration

def wing_a():

    import view_wing_A

def wing_b():

    import view_wing_B
def search():

    import search_dept_arr
def update_gp():
    import search_update_by_gatepass_id

my_menu = Menu(root)

root.config(menu=my_menu)

file_menu = Menu(my_menu)
search_menu = Menu(my_menu)
view_menu = Menu(my_menu)
edit_menu = Menu(my_menu)
my_menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New', command=our_command)
my_menu.add_cascade(label='Search', menu=search_menu)
search_menu.add_command(label='Search Details', command=search)
my_menu.add_cascade(label='View', menu=view_menu)
view_menu.add_command(label='Wing A', command=wing_a)
view_menu.add_command(label='Wing B', command=wing_b)
my_menu.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Update', command=update_gp)
frame = Frame(root, width=100, height=100, bg="#57a1f8")
frame.place(x=800, y=5)

Button(frame, width=10, pady=3, text='Log Out', bg='orange', fg='Black', border=2, command=signout).place(x=30, y=30)

root.mainloop()
