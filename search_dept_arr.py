from tkinter import *
from tkinter import messagebox
from mysql.connector import cursor
from tkcalendar import DateEntry
from datetime import date
import mysql.connector

import tkinter as tk
from tkinter import ttk
from datetime import datetime
root = Tk()
root.title('search')
root.geometry('925x500+300+200')

root.configure(bg='#FFFF8F')
root.resizable(FALSE,FALSE)

db = mysql.connector.connect(host="localhost", user='root',
                                 password='Root#123',
                                 database="pythondata")
cur=db.cursor()

heading = Label(root, text='SEARCH DATE WISE', fg='black', bg='#FFFF8F', font=('Times new roman', 23, 'bold'))
heading.place(x=300, y=15)



def func():
    depart_date= cal.get()
    datetimeobject = datetime.strptime(depart_date,'%m/%d/%y')
    print(datetimeobject)
    new_format_depart = datetimeobject.strftime('%y-%m-%d')
    arrival_date = cal1.get()
    datetimeobject1 = datetime.strptime(arrival_date, '%m/%d/%y')
    print(datetimeobject1)
    new_format_arrival = datetimeobject1.strftime('%y-%m-%d')
    if new_format_depart>new_format_arrival:
        messagebox.showerror("Invalid","Arrival date should be greater than Departure date")
    else:
        sql = "select student_hostel_gate_pass.hostel_gate_pass_id,student_hostel_gate_pass.student_name, student_hostel_gate_pass.stud_email,student_hostel_gate_pass.stud_wing,student_hostel_gate_pass.stud_room_no,student_hostel_gate_pass.mobile_no,student_hostel_gate_pass.reason_for_leave, student_hostel_gate_pass.departure_date,student_hostel_gate_pass.arrival_date, student_hostel_gate_pass.departure_time,student_hostel_gate_pass.arrival_time,stud_parents_info.stud_parent_name ,stud_parents_info.stud_parent_relation,stud_parents_info.parent_mobile_no ,stud_parents_info.parent_address,stud_parents_info.is_gate_pass_approved from student_hostel_gate_pass,stud_parents_info where (departure_date>='"+new_format_depart+"'" +"AND arrival_date<='"+new_format_arrival+"'"")AND(student_hostel_gate_pass.hostel_gate_pass_id=stud_parents_info.hostel_gate_pass_id) "
        cur.execute(sql)
        tree=ttk.Treeview(root)
        tree['show']='headings'
        s=ttk.Style(root)
        s.theme_use("clam")
        s.configure(" ",font=("helevita",10))
        s.configure("Treeview.Heading",foreground='red',font=("helevita",10))

        tree["columns"]=("Gate_Pass_Id","Student_Name","email","wing","Room_no","Mobile_No","Reason_For_Leave","Departure_Date","Arrival_Date","Departure_Time","Arrival_Time","Parent_name","relation","Parent_Contact_no","Parent_address","Is_GatePass_Generated")

        tree.column("Gate_Pass_Id",width=150,minwidth=150,anchor=tk.CENTER)
        tree.column("Student_Name",width=100,minwidth=150,anchor=tk.CENTER)
        tree.column("email",width=200,minwidth=200,anchor=tk.CENTER)
        tree.column("wing",width=50,minwidth=50,anchor=tk.CENTER)
        tree.column("Room_no",width=80,minwidth=80,anchor=tk.CENTER)
        tree.column("Mobile_No",width=100,minwidth=100,anchor=tk.CENTER)
        tree.column("Reason_For_Leave",width=150,minwidth=150,anchor=tk.CENTER)
        tree.column("Departure_Date", width=150,minwidth=150, anchor=tk.CENTER)
        tree.column("Arrival_Date",width=150,minwidth=150, anchor=tk.CENTER)
        tree.column("Departure_Time", width=150, minwidth=150, anchor=tk.CENTER)
        tree.column("Arrival_Time", width=150, minwidth=150, anchor=tk.CENTER)
        tree.column("Parent_name", width=200, minwidth=200, anchor=tk.CENTER)
        tree.column("relation", width=200, minwidth=200, anchor=tk.CENTER)
        tree.column("Parent_Contact_no", width=150, minwidth=150, anchor=tk.CENTER)
        tree.column("Parent_address", width=200, minwidth=200, anchor=tk.CENTER)
        tree.column("Is_GatePass_Generated", width=200, minwidth=200, anchor=tk.CENTER)

        tree.heading("Gate_Pass_Id",text="Gate Pass Id",anchor=tk.CENTER)
        tree.heading("Student_Name",text="Student Name",anchor=tk.CENTER)
        tree.heading("email",text="EmailID",anchor=tk.CENTER)
        tree.heading("wing",text="Wing",anchor=tk.CENTER)
        tree.heading("Room_no",text="Room no",anchor=tk.CENTER)
        tree.heading("Mobile_No",text="Mobile No",anchor=tk.CENTER)
        tree.heading("Reason_For_Leave",text="Reason For Leave",anchor=tk.CENTER)
        tree.heading("Departure_Date",text="Departure Date",anchor=tk.CENTER)
        tree.heading("Arrival_Date",text="Arrival Date",anchor=tk.CENTER)
        tree.heading("Departure_Time",text="Departure Time",anchor=tk.CENTER)
        tree.heading("Arrival_Time",text="Arrival Time",anchor=tk.CENTER)
        tree.heading("Parent_name", text="Parent Name", anchor=tk.CENTER)
        tree.heading("relation", text="Parent/Guardian Relation", anchor=tk.CENTER)
        tree.heading("Parent_Contact_no", text="Parent Contact_No", anchor=tk.CENTER)
        tree.heading("Parent_address", text="Parent Address", anchor=tk.CENTER)
        tree.heading("Is_GatePass_Generated", text="Is GatePass Generated", anchor=tk.CENTER)

        i=0
        for row in cur:
            tree.insert('',i,text="",values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15]))
            i=i+1

        hsb=ttk.Scrollbar(root,orient="horizontal")
        hsb.configure(command=tree.xview)
        tree.configure(xscrollcommand=hsb.set)
        hsb.pack(fill=X,side=BOTTOM)

        tree.pack()

departure_date = Label(root, text="Departure Date", width=13, bg='#FFFF8F', font=("Calibri", 16))
departure_date.place(x=120, y=100)
cal = DateEntry(root, selectmode='day')
cal.config(width=25)
cal.place(x=130, y=130)
dt = date(2023, 5, 15)
cal.set_date(dt)


arrival_date = Label(root, text="Arrival Date", width=13, bg='#FFFF8F', font=("Calibri", 16))
arrival_date.place(x=510, y=100)
cal1 = DateEntry(root, selectmode='day')
cal1.config(width=25)
cal1.place(x=530, y=130)
dt = date(2023, 5, 15)
cal1.set_date(dt)
a = Button(root, width=20, pady=5, text='Search', bg='#93C572', fg='black', font=('Calibri', 12, 'bold'),
                   border=2, command=func)
a.place(x=350, y=180)
root.mainloop()