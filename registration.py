import tkinter
from tkinter import *
from tkinter import messagebox

from mysql.connector import cursor
from tkcalendar import DateEntry
from datetime import date
import mysql.connector
from datetime import datetime
import re
from validate_email import validate_email
import phonenumbers

root = Tk()
root.title('Registration Page')
root.geometry('1000x600+300+200')

root.configure(bg='#FFFF8F')
root.resizable(False, False)

heading = Label(root, text='LEAVE APPLICATION', fg='black', bg='#FFFF8F', font=('Times new roman', 23, 'bold'))
heading.place(x=300, y=15)


########################## name ################3
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
name.place(x=100, y=70)
nm = Entry(root, width=30, fg='black', border=2, bg="#F5F5DC", font=('Microsoft YaHei UI Light', 11))
nm.focus_set()
nm.bind('<FocusOut>', validation_name)
nm.place(x=130, y=100)

# Frame(root,width=230,height=2,bg='black').place(x=149,y=94)

################################# wing ######################3


"""vars = StringVar()
Radiobutton(root, text="Wing A", padx=6, variable=vars, bg="#FFFF8F", font=("Calibri", 16), value="Wing A").place(x=130,
                                                                                                                y=150)
Radiobutton(root, text="Wing B", padx=10, variable=vars, bg="#FFFF8F", font=("Calibri", 16), value="Wing B").place(x=240,
                                                                                                                 y=150)
wing = Label(root, text="Wing ", width=10, bg='#FFFF8F', font=("Calibri", 16))

wing.place(x=100, y=130)"""

def validation_wing(event):
    n = wig.get()
    msg = ''
    try:
        if not len(n)==0:
            if len(n) > 1:
                msg = 'You are allowed to Type A or B only For Wing'
                messagebox.showerror('message', msg)
            else:
                pass

    except Exception as ep:
            messagebox.showerror('error', ep)

wing = Label(root, text="Wing A/B", width=10, bg='#FFFF8F', font=("Calibri", 16))
wing.place(x=110, y=130)
wig = Entry(root, width=25, fg='black', border=2, bg="#F5F5DC", font=('Microsoft YaHei UI Light', 11))
wig.bind('<FocusOut>', validation_wing)
wig.place(x=130, y=160)
###############################################################
def validation_room(event):
    n = rm.get()
    msg = ''
    special_char = '[@_!$%^&*()<>?/\|}{~:]#'
    if not len(n) == 0:

        try:
            if any(ch.isalpha() for ch in n):
                msg = 'Room can\'t have Alphabets'
                messagebox.showinfo('message', msg)
            elif len(n) < 3:
                msg = 'Room Number is too short.'
                messagebox.showinfo('message', msg)
            elif len(n) > 3:
                msg = ' Room number is too long.'
                messagebox.showinfo('message', msg)


            elif any(c in special_char for c in n):
                msg = "Room Number can\'t  have special characters"
                messagebox.showinfo('message', msg)
            else:
                pass

        except Exception as ep:
            messagebox.showerror('error', ep)

room = Label(root, text="Room No", width=10, bg='#FFFF8F', font=("Calibri", 16))
room.place(x=495, y=130)
rm = Entry(root, width=25, fg='black', border=2, bg="#F5F5DC", font=('Microsoft YaHei UI Light', 11))
rm.bind('<FocusOut>', validation_room)
rm.place(x=510, y=160)


###############################################################



def check(event):
    n = em.get()
    msg = ''
    if not len(n)==0:
        is_valid = validate_email(n)

        if is_valid:
            pass
        else:
            msg = 'Invalid  email address'
            messagebox.showinfo('message', msg)


email = Label(root, text="Email Id", width=10, bg='#FFFF8F', font=("Calibri", 16))
email.place(x=490, y=70)
em = Entry(root, width=30, fg='black', border=2, bg="#F5F5DC", font=('Microsoft YaHei UI Light', 11))

em.bind('<FocusOut>',check)
em.place(x=510, y=100)

def check_mob(event):
    x = mob.get()
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
            msg = 'Invalid phone number -10 digits required'
            messagebox.showinfo('message', msg)


mobile_no = Label(root, text="Mobile No", width=13, bg='#FFFF8F', font=("Calibri", 16))
mobile_no.place(x=100, y=200)
mob = Entry(root, width=25, fg='black', border=2, bg="#F5F5DC", font=('Microsoft YaHei UI Light', 11))
mob.bind('<FocusOut>',check_mob)
mob.place(x=130, y=230)

def validation_reason(event):
    n = reas.get()
    msg = ''
    try:
        if not len(n)==0:
            if len(n) <= 2:
                msg = 'Reason is too short.'
                messagebox.showinfo('message', msg)
            elif len(n) > 100:
                msg = 'Reason is too long.'
                messagebox.showinfo('message', msg)
            else:
                pass

    except Exception as ep:
            messagebox.showerror('error', ep)
reason = Label(root, text="Reason For Leave", width=13, bg='#FFFF8F', font=("Calibri", 16))
reason.place(x=510, y=200)
reas = Entry(root, width=35, fg='black', border=2, bg="#F5F5DC", font=('Microsoft YaHei UI Light', 11))
reas.bind('<FocusOut>',validation_reason)
reas.place(x=510, y=230)

departure_date = Label(root, text="Departure Date", width=13, bg='#FFFF8F', font=("Calibri", 16))
departure_date.place(x=120, y=260)
cal = DateEntry(root)
cal.config(width=25)
cal.place(x=130, y=300)
# dt = date(2023, 5, 15)
# cal.set_date(dt)

arrival_date = Label(root, text="Arrival Date", width=13, bg='#FFFF8F', font=("Calibri", 16))
arrival_date.place(x=490, y=260)
cal1 = DateEntry(root)
cal1.config(width=25)
cal1.place(x=510, y=300)

def on_enter(e):
    drr.delete(0, 'end')
def departTimecheck(event):
    dtime=drr.get()
    msg=''
    if not len(dtime)==0:
        try:
            regex = '^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$'
            regex_Twenty_four_Hour="([01]?[0-9]|2[0-3]):[0-5][0-9]"
            match = re.search(regex_Twenty_four_Hour, drr.get())
            if match:
                pass
            else:
                msg = 'Invalid Departure time'
                messagebox.showinfo('message', msg)
        except Exception as ep:
            messagebox.showerror('error', ep)
departure_time = Label(root, text="Departure Time", width=13, bg='#FFFF8F', font=("Calibri", 16))
departure_time.place(x=120, y=330)
drr = Entry(root, width=25, fg='black', border=2, bg="#F5F5DC", font=('Microsoft YaHei UI Light', 11))
drr.insert(0, 'HH:MM(24-Hour)')
drr.bind('<FocusIn>', on_enter)
drr.bind('<FocusOut>',departTimecheck)
drr.place(x=130, y=360)

def on_enterarr(e):
    arr.delete(0, 'end')

def arrivalTimecheck(event):
    atime=arr.get()
    msg=''
    if not len(atime)==0:
        try:
            regex = '^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$'
            regex_twenty_Four="([01]?[0-9]|2[0-3]):[0-5][0-9]"
            match = re.search(regex_twenty_Four, arr.get())
            if match:
                pass
            else:
                msg = 'Invalid Arrival time'
                messagebox.showinfo('message', msg)
        except Exception as ep:
            messagebox.showerror('error', ep)
arrival_time = Label(root, text="Arrival Time ", width=13, bg='#FFFF8F', font=("Calibri", 16))
arrival_time.place(x=490, y=330)
arr = Entry(root, width=25, fg='black', border=2, bg="#F5F5DC", font=('Microsoft YaHei UI Light', 11))
arr.insert(0, 'HH:MM(24 Hour)')
arr.bind('<FocusIn>', on_enterarr)
arr.bind('<FocusOut>',arrivalTimecheck)
arr.place(x=510, y=360)

db = mysql.connector.connect(host="localhost", user='root',
                             password='Root#123',
                             database="pythondata")
cursor = db.cursor()
now = datetime.now()

current_time = now.strftime("%H:%M:%S")


# "GatePass"+vars.get()+current_time
def next():
    if nm.get() == "" or em.get() == "" or rm.get() == "" or mob.get() == "" or reas.get() == "" or drr.get() == "" or arr.get() == "":
        messagebox.showerror("invalid", "please enter details")

    else:
        try:
            depart_date = cal.get()

            print("Date", cal.get_date())
            datetimeobject = datetime.strptime(depart_date, '%m/%d/%y')
            print(datetimeobject)
            new_format_depart = datetimeobject.strftime('%y-%m-%d')

            arrival_date = cal1.get()
            datetimeobject1 = datetime.strptime(arrival_date, '%m/%d/%y')
            print(datetimeobject1)
            new_format_arrival = datetimeobject1.strftime('%y-%m-%d')

            print(nm.get(), em.get(), rm.get(), mob.get(), reas.get(),wig.get(), new_format_depart, new_format_arrival, drr.get(),
                  arr.get())
            if new_format_depart > new_format_arrival:
                messagebox.showerror("Invalid", "Arrival date should be greater than Departure date")
            else:
                data = ("GatePass" + date.today().strftime('%y-%m-%d')+current_time, nm.get(), em.get(), wig.get(), rm.get(), mob.get(), reas.get(),
                    new_format_depart, new_format_arrival, drr.get(), arr.get())
                cursor.execute(
                "INSERT IGNORE INTO student_hostel_gate_pass(hostel_gate_pass_id, student_name, stud_email,stud_wing,stud_room_no,mobile_no, reason_for_leave, departure_date,arrival_date, departure_time,arrival_time) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",
                data)

                messagebox.showinfo("valid", "Student Registered succesfully")

                print("Query Executed successfully")
                db.commit()

        except Exception as e:
            print(e)


        root.destroy()
        import parentInfo


a = tkinter.Button(root, width=20, pady=5, text='Save & Next', bg='#93C572', fg='black', font=('Calibri', 12, 'bold'),
                   border=2, command=next)
a.place(x=400, y=450)


def home():
    import menuPage
    root.destroy()




b = tkinter.Button(root, width=15, pady=5, text='Home', bg='orange', fg='black', font=('Calibri', 10, 'bold'), border=2,
                   command=home)
b.place(x=5, y=5)
root.mainloop()
