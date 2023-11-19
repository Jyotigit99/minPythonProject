from tkinter import *
from tkinter import messagebox
import mysql.connector
from mysql.connector import cursor
from tkcalendar import DateEntry
from datetime import date

import tkinter as tk
from tkinter import ttk

root = Tk()
root.title('Wing A')
root.geometry('925x500+300+200')
#root.configure(bg='#fff')
root.configure(bg='#FFFF8F')
#root.resizable(False, False)

db = mysql.connector.connect(host="localhost", user='root',
                                 password='Root#123',
                                 database="pythondata")
cur=db.cursor()
sql="select  student_hostel_gate_pass.hostel_gate_pass_id,student_name, stud_email,stud_wing,stud_room_no,mobile_no, reason_for_leave, departure_date,arrival_date, departure_time,arrival_time,stud_parent_name ,stud_parent_relation,parent_mobile_no ,parent_address,is_gate_pass_approved from student_hostel_gate_pass,stud_parents_info  where stud_wing='A' AND stud_wing='a' AND student_hostel_gate_pass.hostel_gate_pass_id=stud_parents_info.hostel_gate_pass_id"
cur.execute(sql)

tree=ttk.Treeview(root)
tree['show']='headings'
s=ttk.Style(root)
s.theme_use("clam")
s.configure(" ",font=("helevita",10))
s.configure("Treeview.Heading",foreground='red',font=("helevita",10))

tree["columns"]=("Gate_Pass_Id","Student_Name","email","wing","Room_no","Mobile_No","Reason_For_Leave","Departure_Date","Arrival_Date","Departure_Time","Arrival_Time","Parent_name","relation","Parent_Contact_no","Parent_address","Gate Pass status")

tree.column("Gate_Pass_Id",width=150,minwidth=150,anchor=tk.CENTER)
tree.column("Student_Name",width=100,minwidth=150,anchor=tk.CENTER)
tree.column("email",width=200,minwidth=200,anchor=tk.CENTER)
tree.column("wing",width=50,minwidth=50,anchor=tk.CENTER)
tree.column("Room_no",width=80,minwidth=80,anchor=tk.CENTER)
tree.column("Mobile_No",width=100,minwidth=100,anchor=tk.CENTER)
tree.column("Reason_For_Leave",width=150,minwidth=150,anchor=tk.CENTER)
tree.column("Departure_Date",width=150,minwidth=150,anchor=tk.CENTER)
tree.column("Arrival_Date",width=150,minwidth=150,anchor=tk.CENTER)
tree.column("Departure_Time",width=150,minwidth=150,anchor=tk.CENTER)
tree.column("Arrival_Time",width=150,minwidth=150,anchor=tk.CENTER)
tree.column("Parent_name", width=200, minwidth=200, anchor=tk.CENTER)
tree.column("relation", width=200, minwidth=200, anchor=tk.CENTER)
tree.column("Parent_Contact_no", width=150, minwidth=150, anchor=tk.CENTER)
tree.column("Parent_address", width=200, minwidth=200, anchor=tk.CENTER)
tree.column("Gate Pass status", width=200, minwidth=200, anchor=tk.CENTER)

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
tree.heading("Gate Pass status", text="Gate Pass status", anchor=tk.CENTER)

i=0
for row in cur:
    tree.insert('',i,text="",values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15]))
    i=i+1

hsb=ttk.Scrollbar(root,orient="horizontal")
hsb.configure(command=tree.xview)
tree.configure(xscrollcommand=hsb.set)
hsb.pack(fill=X,side=BOTTOM)

tree.pack()






root.mainloop()