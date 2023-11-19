import tkinter
from tkinter import *
from tkinter import messagebox
from mysql.connector import cursor
from tkcalendar import DateEntry
from datetime import date
import mysql.connector
from datetime import datetime
import re

root = Tk()
root.title('Parents Information')
root.geometry('1000x600+300+200')

root.configure(bg='#FFFF8F')
root.resizable(False, False)

heading = Label(root, text='PARENTS INFORMATION', fg='Black', bg='#FFFF8F', font=('Calibri', 23, 'bold'))
heading.place(x=350, y=20)

def validation_name(event):
    n = nm.get()
    msg = ''
    special_char = '[@_!$%^&*()<>?/\|}{~:]#'
    if not len(n) == 0:

        try:
            if any(ch.isdigit() for ch in n):
                msg = 'Name can\'t have numbers'
                messagebox.showinfo('message', msg)
            elif len(n) <= 2:
                msg = 'name is too short.'
                messagebox.showinfo('message', msg)
            elif len(n) > 100:
                msg = 'name is too long.'
                messagebox.showinfo('message', msg)


            elif any(c in special_char for c in n):
                msg = "Name can\'t  have special characters"
                messagebox.showinfo('message', msg)
            else:
                pass

        except Exception as ep:
            messagebox.showerror('error', ep)

name = Label(root, text=" Name", width=10, bg='#FFFF8F', font=("Calibri", 16))
name.place(x=100, y=90)
nm = Entry(root, width=30, fg='black', border=2, bg="#F5F5DC", font=('Microsoft YaHei UI Light', 11))
nm.focus_set()
nm.bind('<FocusOut>', validation_name)
nm.place(x=130, y=120)

def validation_relation(event):
    n = rel.get()
    msg = ''
    special_char = '[@_!$%^&*()<>?/\|}{~:]#'
    if not len(n) == 0:

        try:
            if any(ch.isdigit() for ch in n):
                msg = 'relation field can\'t have numbers'
                messagebox.showinfo('message', msg)
            elif len(n) <= 2:
                msg = 'relation field is too short.'
                messagebox.showinfo('message', msg)
            elif len(n) > 100:
                msg = 'relation field is too long.'
                messagebox.showinfo('message', msg)


            elif any(c in special_char for c in n):
                msg = "relation field can\'t  have special characters"
                messagebox.showinfo('message', msg)
            else:
                pass

        except Exception as ep:
            messagebox.showerror('error', ep)

relation = Label(root, text="Relation", width=10, bg='#FFFF8F', font=("Calibri", 16))
relation.place(x=500, y=90)
rel = Entry(root, width=30, fg='black', border=2, bg="#F5F5DC", font=('Microsoft YaHei UI Light', 11))
rel.bind('<FocusOut>', validation_relation)
rel.place(x=500, y=120)

def check_mob(event):
    x = cn.get()
    msg=''
    if not len(x)==0:
        phone_regex = '^(\+91|\+91\-|0)?[6789]\d{9}$'

        match = re.search(phone_regex, x)
        if any(ch.isalpha() for ch in x):
            msg = 'Mobile can\'t have alphabets'
            messagebox.showinfo('message', msg)
        elif match:
            pass
        else:
            msg = 'Invalid phone number- 10 digits required'
            messagebox.showinfo('message', msg)
Contact_no = Label(root, text="Mobile No", width=10, bg='#FFFF8F', font=("Calibri", 16))
Contact_no.place(x=120, y=160)
cn = Entry(root, width=30, fg='black', border=2, bg="#F5F5DC", font=('Microsoft YaHei UI Light', 11))
cn.bind('<FocusOut>',check_mob)
cn.place(x=130, y=190)

def validation_address(event):
    n = addr.get()
    msg = ''

    if not len(n) == 0:

        try:
            if len(n) < 3:
                msg = 'Address is too short.'
                messagebox.showinfo('message', msg)
            elif len(n) > 50:
                msg = ' Address is too long.'
                messagebox.showinfo('message', msg)

            else:
                pass

        except Exception as ep:
            messagebox.showerror('error', ep)

address = Label(root, text=" Address", width=10, bg='#FFFF8F', font=("Calibri", 16))
address.place(x=500, y=160)
addr = Entry(root, width=30, fg='black', border=2, bg="#F5F5DC", font=('Microsoft YaHei UI Light', 11))
addr.bind('<FocusOut>',validation_address)
addr.place(x=500, y=190)

db = mysql.connector.connect(host="localhost", user='root',
                                 password='Root#123',
                                 database="pythondata")
cursor = db.cursor()
'''def noentry():
    if nm.get()==""or rel.get()==""or cn.get()==""or addr.get()=="":
        messagebox.showerror("invalid","please enter details")
    else:
        try:
          print(nm.get(), rel.get(), cn.get(), addr.get())
          cursor.execute(
              "select  hostel_gate_pass_id from student_hostel_gate_pass where hostel_gate_pass_id=(SELECT LAST_INSERT_ID())  ORDER BY hostel_gate_pass_id DESC LIMIT 1")
          hostel_id = cursor.fetchone();
          if hostel_id:
              print(hostel_id)

          data = (hostel_id[0], nm.get(), rel.get(), cn.get(), addr.get(),vars.get())
          cursor.execute(
            "INSERT INTO stud_parents_info(hostel_gate_pass_id, stud_parent_name, stud_parent_relation,parent_mobile_no,parent_address,is_gate_pass_approved ) VALUES (%s,%s,%s,%s,%s,%s);",
                data)

          messagebox.showerror("Not Saved", "Your Application is not approved")

          print("Query Executed successfully")
          db.commit()
        except Exception as e:

            print(e)

    root.destroy()
    import menuPage'''

'''def okentry():
    if nm.get()==""or rel.get()==""or cn.get()==""or addr.get()=="":
        messagebox.showerror("invalid","please enter details")
    elif not appr.get()=='Yes'or appr.get()=='yes'or appr.get()=='No'or appr.get()=='no':
        messagebox.showerror("Incorrect", "You are allowed to type only Yes or No")
    else:
        try:
          print(nm.get(), rel.get(), cn.get(), addr.get())
          cursor.execute(
              "select  hostel_gate_pass_id from student_hostel_gate_pass where hostel_gate_pass_id=(SELECT LAST_INSERT_ID())  ORDER BY hostel_gate_pass_id DESC LIMIT 1")
          hostel_id = cursor.fetchone();
          if hostel_id:
              print(hostel_id)

          data = (hostel_id[0], nm.get(), rel.get(), cn.get(), addr.get(),appr.get())
          cursor.execute(
            "INSERT INTO stud_parents_info(hostel_gate_pass_id, stud_parent_name, stud_parent_relation,parent_mobile_no,parent_address,is_gate_pass_approved ) VALUES (%s,%s,%s,%s,%s,%s);",
                data)

          messagebox.showinfo("valid", "data is enter successfully")

          print("Query Executed successfully")
          db.commit()
        except Exception as e:

            print(e)'''


def next():
    if nm.get() == "" or rel.get() == "" or cn.get() == "" or addr.get() == ""or appr.get()=="":
        messagebox.showerror("invalid", "please enter details")
    elif (appr.get() == "Yes" or appr.get() == "YES") :
        try:
          print(nm.get(), rel.get(), cn.get(), addr.get())
          cursor.execute(
              "select  hostel_gate_pass_id from student_hostel_gate_pass where hostel_gate_pass_id=(SELECT LAST_INSERT_ID())  ORDER BY hostel_gate_pass_id DESC LIMIT 1")
          hostel_id = cursor.fetchone();
          if hostel_id:
              print(hostel_id)

          data = (hostel_id[0], nm.get(), rel.get(), cn.get(), addr.get(),appr.get())
          cursor.execute(
                    "INSERT INTO stud_parents_info(hostel_gate_pass_id, stud_parent_name, stud_parent_relation,parent_mobile_no,parent_address,is_gate_pass_approved ) VALUES (%s,%s,%s,%s,%s,%s);",
                    data)

          messagebox.showinfo("valid", "Your Application is improved..Please generate Gate Pass")

          print("Query Executed successfully")
          db.commit()
        except Exception as e:

            print(e)


        root.destroy()
        import GatePass
    elif  (appr.get() == "No" or appr.get() == "NO"):
        try:
          print(nm.get(), rel.get(), cn.get(), addr.get())
          cursor.execute(
              "select  hostel_gate_pass_id from student_hostel_gate_pass where hostel_gate_pass_id=(SELECT LAST_INSERT_ID())  ORDER BY hostel_gate_pass_id DESC LIMIT 1")
          hostel_id = cursor.fetchone();
          if hostel_id:
              print(hostel_id)

          data = (hostel_id[0], nm.get(), rel.get(), cn.get(), addr.get(),appr.get())
          cursor.execute(
                    "INSERT INTO stud_parents_info(hostel_gate_pass_id, stud_parent_name, stud_parent_relation,parent_mobile_no,parent_address,is_gate_pass_approved ) VALUES (%s,%s,%s,%s,%s,%s);",
                    data)

          messagebox.showinfo("valid", "Your Application is not Approved")

          print("Query Executed successfully")
          db.commit()
        except Exception as e:

            print(e)


        root.destroy()
        import menuPage

    else:
        messagebox.showerror("Incorrect", "You are allowed to type only Yes or No For Approved")

approved = Label(root, text="Do you want to approved (Type Yes/No)", width=50, bg="#FFFF8F", font=("Calibri", 16))
approved.place(x=15, y=270)
appr = Entry(root, width=10, fg='black', border=2, bg="#F5F5DC", font=('Microsoft YaHei UI Light', 11))
appr.place(x=500, y=275)
#vars = StringVar()
"""Radiobutton(root, text="Yes", padx=6, variable=vars, bg="#FFFF8F", font=("Calibri", 16), value="Yes",command=okentry).place(x=440, y=270)
Radiobutton(root, text="No", padx=10, variable=vars, bg="#FFFF8F", font=("Calibri", 16), value="No", command=noentry).place(
    x=500, y=270)"""





a = tkinter.Button(root, width=15, pady=5, text='Gate Pass', bg='#93C572', fg='black', font=('Calibri', 12, 'bold'),
                   border=2, command=next)
a.place(x=470, y=350)


def home():
    root.destroy()
    import registration


a = tkinter.Button(root, width=15, pady=5, text='Back', bg='orange', fg='black', font=('Calibri', 12, 'bold'), border=2,
                   command=home)
a.place(x=330, y=350)

root.mainloop()
