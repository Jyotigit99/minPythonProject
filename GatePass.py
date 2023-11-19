import tkinter
from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import date
from mysql.connector import cursor
import mysql.connector
import datetime
import smtplib

root = Tk()
root.title('Gate Pass')
root.geometry('1000x600+300+200')

root.configure(bg='#FFFF8F')
root.resizable(False, False)

heading = Label(root, text='GATE PASS', fg='black', bg='#FFFF8F', font=('Times new roman', 40, 'bold'))
heading.place(x=340, y=15)
db = mysql.connector.connect(host="localhost", user='root',
                             password='Root#123',
                             database="pythondata")
cursor = db.cursor()
try:

    cursor.execute(
        "select  hostel_gate_pass_id,student_name,stud_wing,stud_room_no,departure_date,arrival_date,stud_email,departure_time,arrival_time from student_hostel_gate_pass where hostel_gate_pass_id=(SELECT LAST_INSERT_ID())  ORDER BY hostel_gate_pass_id DESC LIMIT 1")
    hostel_id = cursor.fetchone();
    if hostel_id:
        print(type(hostel_id))

    data = (hostel_id[0], hostel_id[1],hostel_id[2],hostel_id[3],hostel_id[4],hostel_id[5],hostel_id[6],hostel_id[7],hostel_id[8])


    db.commit()
except Exception as e:

    print(e)

name = Label(root, text=" Name", width=10, bg='#FFFF8F', font=("Calibri", 16))
name.place(x=100, y=100)
nm = Entry(root, width=30, fg='black', border=2, bg="#F5F5DC", font=('Microsoft YaHei UI Light', 11))
nm.insert(0, hostel_id[1])
nm.config(state=DISABLED)
nm.place(x=130, y=130)

wing = Label(root, text="Wing", width=13, bg='#FFFF8F', font=("Calibri", 16))
wing.place(x=85, y=170)
wig = Entry(root, width=30, fg='black', border=2, bg="#F5F5DC", font=('Microsoft YaHei UI Light', 11))
wig.insert(0, hostel_id[2])
wig.config(state=DISABLED)
wig.place(x=130, y=200)

room_no = Label(root, text="Room No", width=10, bg='#FFFF8F', font=("Calibri", 16))
room_no.place(x=515, y=170)
rm = Entry(root, width=30, fg='black', border=2, bg="#F5F5DC", font=('Microsoft YaHei UI Light', 11))
rm.insert(0, hostel_id[3])
rm.config(state=DISABLED)
rm.place(x=530, y=200)

depart = Label(root, text="Departure Date", width=20, bg='#FFFF8F', font=("Calibri", 16))
depart.place(x=90, y=240)
dept = Entry(root, width=30, fg='black', border=2, bg="#F5F5DC", font=('Microsoft YaHei UI Light', 11))
depart_date= hostel_id[4]


new_format_depart = depart_date.strftime('%y-%m-%d')
print(new_format_depart)

dept.insert(0, new_format_depart)
dept.config(state=DISABLED)
dept.place(x=130, y=270)

arrival = Label(root, text="Arrival Date", width=20, bg='#FFFF8F', font=("Calibri", 16))
arrival.place(x=470, y=240)
arr = Entry(root, width=30, fg='black', border=2, bg="#F5F5DC", font=('Microsoft YaHei UI Light', 11))
arrival_date= hostel_id[5]


new_format_arrival = arrival_date.strftime('%y-%m-%d')
print(new_format_depart)
arr.insert(0, new_format_arrival)
arr.config(state=DISABLED)
arr.place(x=530, y=270)

Gate_id = Label(root, text="Gate Pass ID", width=10, bg='#FFFF8F', font=("Calibri", 16))
Gate_id.place(x=520, y=100)
gid = Entry(root, width=30, fg='black', border=2, bg="#F5F5DC", font=('Microsoft YaHei UI Light', 11))
gid.insert(0, hostel_id[0])
gid.config(state=DISABLED)
gid.place(x=530, y=130)


def send_message():
    sender_email='jyotijk1999@gmail.com'
    sender_password='hcicejhgauvieygi'
    server= smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(sender_email,sender_password)

    receiaddress=hostel_id[6]

    email_body= "************************* Hi This is Your Gate Pass *********************"+"\n\n\n"+"Gate Pass ID:"+" "+hostel_id[0]+"\n\n\n"+"Name Of the student:"+" "+" "+hostel_id[1]+"\n\n\n"+"Wing:"+" "+hostel_id[2]+"\n\n\n"+"Room Number:"+" "+f'{hostel_id[3]}'+"\n\n\n"+"Departure Date:"+" "+new_format_depart+"\n\n\n"+"Arrival Date:"+" "+new_format_arrival+"\n\n\n"+"Departure Time:"+" "+hostel_id[7]+"\n\n\n"+"Arrival Time:"+" "+hostel_id[8]+"\n\n\n\n\n\n\n\n\n\n\n"+"From,"+"\n\n\n\n\n"+"JSPM Girls Hostel"
    message = 'Subject: {}\n\n{}'.format("JSPM Girls Hostel GatePass", email_body)
    server.sendmail(sender_email,receiaddress,message)
    messagebox.showinfo("Email", "Send Email")
    root.destroy()
    import menuPage

a=tkinter.Button(root, width=20, pady=5, text='Send Email', bg='#93C572', fg='black', font=('Calibri', 12, 'bold'),
                 border=2,command=send_message)
a.place(x=400, y=350)
root.mainloop()
