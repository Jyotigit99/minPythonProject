from tkinter import *
from tkinter import messagebox
from mysql.connector import cursor
from tkcalendar import DateEntry
from datetime import date
import mysql.connector

import tkinter as tk
from tkinter import ttk
from datetime import datetime
import smtplib

root = Tk()
root.title('search_update_by_gatePass_id')
root.geometry('955x600+300+200')

root.configure(bg='#FFFF8F')
root.resizable(FALSE,FALSE)


heading = Label(root, text='SEARCH-UPDATE BY GATEPASS ID ', fg='black', bg='#FFFF8F', font=('Times new roman', 17, 'bold'))
heading.place(x=250, y=15)

db = mysql.connector.connect(host="localhost", user='root',
                             password='Root#123',
                             database="pythondata")
cur=db.cursor()
gatepass_id = Label(root, text="GatePass Id", width=13, bg='#FFFF8F', font=("Calibri", 16))
gatepass_id.place(x=60, y=56)
gate = Entry(root, width=30, fg='black', border=2, bg="#F5F5DC", font=('Microsoft YaHei UI Light', 11))
gate.place(x=210, y=58)

heading = Label(root, text='UPDATE YOUR INFORMATION ', fg='black', bg='#FFFF8F', font=('Times new roman', 17, 'bold'))
heading.place(x=290, y=100)
search_id_data=()
print(len(search_id_data))
email_of_student=""
def next_page():
    gate_Pass_Id_to_Search = gate.get()

    nm.config(state=NORMAL)

    wig.config(state=NORMAL)

    rm.config(state=NORMAL)

    dept.config(state=NORMAL)

    arr.config(state=NORMAL)

    gid.config(state=NORMAL)
    if  gate.get() == "":
        messagebox.showerror("invalid", "please enter Gate Pass Id to search/update")
        nm.delete(0, 'end')
        nm.config(state=DISABLED)
        wig.delete(0, 'end')
        wig.config(state=DISABLED)
        rm.delete(0, 'end')
        rm.config(state=DISABLED)
        dept.delete(0, 'end')
        dept.config(state=DISABLED)
        arr.delete(0, 'end')
        arr.config(state=DISABLED)
        gid.delete(0, 'end')
        gid.config(state=DISABLED)

    else:
        try:
            sql = "select student_hostel_gate_pass.hostel_gate_pass_id, student_name,stud_wing,stud_room_no,departure_date,arrival_date, is_gate_pass_approved,stud_email from student_hostel_gate_pass,stud_parents_info where student_hostel_gate_pass.hostel_gate_pass_id='"+gate_Pass_Id_to_Search+"'" +" AND "+"stud_parents_info.hostel_gate_pass_id='"+gate_Pass_Id_to_Search+"'"

            cur.execute(sql)
            search_id_data = cur.fetchone();
            if search_id_data:
                print(search_id_data[0], search_id_data[1], search_id_data[2], search_id_data[3], search_id_data[4], search_id_data[5], search_id_data[6],search_id_data[7])

                data = (
                    search_id_data[0], search_id_data[1], search_id_data[2], search_id_data[3], search_id_data[4], search_id_data[5], search_id_data[6],search_id_data[7])
                email_of_student=search_id_data[7]
                print(email_of_student)
                nm.delete(0, 'end')
                nm.insert(0, search_id_data[1])
                nm.config(state=DISABLED)
                wig.delete(0, 'end')
                wig.insert(0, search_id_data[2])
                wig.config(state=DISABLED)
                rm.delete(0, 'end')
                rm.insert(0, search_id_data[3])
                rm.config(state=DISABLED)
                dept.delete(0, 'end')
                dept.insert(0, search_id_data[4])
                dept.config(state=DISABLED)
                arr.delete(0, 'end')
                arr.insert(0, search_id_data[5])
                arr.config(state=DISABLED)
                gid.delete(0, 'end')
                gid.insert(0, search_id_data[0])
                gid.config(state=DISABLED)

                db.commit()
            else:
                messagebox.showinfo("Invalid","Invalid Gate Pass ID")

        except Exception as e:

            print(e)


def cancelentry():
    yes =messagebox.askyesno("Cancel","Do you really want to Cancel your gate pass")
    if yes:
         gate_Pass_Id_to_Search = gate.get()
         if nm.get()==""or wig.get()==""or rm.get()==""or dept.get()=="" or arr.get=="":
             messagebox.showerror("invalid","No record found to cancel")
         else:
            try:
                cur.execute(
                    "select is_gate_pass_approved,student_hostel_gate_pass.stud_email from stud_parents_info,student_hostel_gate_pass where stud_parents_info.hostel_gate_pass_id='" + gate_Pass_Id_to_Search + "'" + "AND stud_parents_info.is_gate_pass_approved='cancel' AND student_hostel_gate_pass.hostel_gate_pass_id=stud_parents_info.hostel_gate_pass_id")
                hostel_id = cur.fetchone();
                cur.execute(
                    "select is_gate_pass_approved,student_hostel_gate_pass.stud_email from stud_parents_info,student_hostel_gate_pass where stud_parents_info.hostel_gate_pass_id='" + gate_Pass_Id_to_Search + "'" + "AND stud_parents_info.is_gate_pass_approved='No' AND student_hostel_gate_pass.hostel_gate_pass_id=stud_parents_info.hostel_gate_pass_id")
                Nostatus = cur.fetchone();
                if hostel_id:
                    messagebox.showinfo("Canceled", "Your GatePass is already canceled")
                    print(hostel_id[1])
                elif Nostatus:
                    messagebox.showinfo("Not Approved", "Your GatePass is Not Approved by Admin")
                else:
                    cur.execute(
                        "select is_gate_pass_approved,student_hostel_gate_pass.stud_email from stud_parents_info,student_hostel_gate_pass where stud_parents_info.hostel_gate_pass_id='" + gate_Pass_Id_to_Search + "'" + "AND stud_parents_info.is_gate_pass_approved='Yes' AND student_hostel_gate_pass.hostel_gate_pass_id=stud_parents_info.hostel_gate_pass_id")
                    hostel_id = cur.fetchone();
                    if hostel_id:
                        cur.execute(
                        "Update stud_parents_info SET is_gate_pass_approved='cancel' where stud_parents_info.hostel_gate_pass_id='"+gate_Pass_Id_to_Search+"'"+" AND stud_parents_info.is_gate_pass_approved='Yes'")


                        messagebox.showerror("Canceled", "Your GatePass is canceled")
                        print("Query Executed successfully")
                        #send email for canceled gate pass
                        print("email",hostel_id[1])



                        sender_email = 'jyotijk1999@gmail.com'
                        sender_password = 'hcicejhgauvieygi'
                        server = smtplib.SMTP('smtp.gmail.com', 587)
                        server.starttls()
                        server.login(sender_email, sender_password)

                        receiaddress = hostel_id[1]

                        email_body = "Hi Your Gate Pass is canceled. Please contact Admin for new Gate Pass if needed"+ "\n\n\n\n\n\n\n\n\n\n\n" + "From," + "\n\n\n\n\n" + "JSPM Girls Hostel"
                        message = 'Subject: {}\n\n{}'.format("JSPM Girls Hostel GatePass", email_body)
                        server.sendmail(sender_email, receiaddress, message)
                        messagebox.showinfo("Email", "Email sent to your respective email id")
                        db.commit()

            except Exception as e:

                print(e)
            root.destroy()
            import menuPage
    else:

        pass


def yesUpdateEntry():
    gate_Pass_Id_to_Search = gate.get()
    try:
        cur.execute(
            "select is_gate_pass_approved,student_hostel_gate_pass.stud_email from stud_parents_info,student_hostel_gate_pass where stud_parents_info.hostel_gate_pass_id='" + gate_Pass_Id_to_Search + "'" + "AND stud_parents_info.is_gate_pass_approved='cancel'AND student_hostel_gate_pass.hostel_gate_pass_id=stud_parents_info.hostel_gate_pass_id")
        hostel_id = cur.fetchone();
        cur.execute(
            "select is_gate_pass_approved,student_hostel_gate_pass.stud_email from stud_parents_info,student_hostel_gate_pass where stud_parents_info.hostel_gate_pass_id='" + gate_Pass_Id_to_Search + "'" + "AND stud_parents_info.is_gate_pass_approved='No'AND student_hostel_gate_pass.hostel_gate_pass_id=stud_parents_info.hostel_gate_pass_id")
        Nostatus = cur.fetchone();
        if hostel_id:
            messagebox.showinfo("Sorry", "No Update Allowed..Gate Pass is already canceled ")
            print(hostel_id[1])
        elif Nostatus:
            messagebox.showinfo("Sorry", "No Update Allowed..Gate Pass is  Not Approved")

        else:
            messagebox.showinfo("Update", "You are allowed to change only Departure/Arrival dates")
            dept.config(state=NORMAL)
            arr.config(state=NORMAL)
            update.config(state=NORMAL)
    except Exception as e:

        print(e)




def update_GatePass():
    gate_Pass_Id_to_Search=gate.get()
    depart_date = dept.get()

    datetimeobject = datetime.strptime(depart_date, '%m/%d/%y')
    print(datetimeobject)
    new_format_depart = datetimeobject.strftime('%y-%m-%d')

    arrival_date = arr.get()
    datetimeobject1 = datetime.strptime(arrival_date, '%m/%d/%y')
    print(datetimeobject1)
    new_format_arrival = datetimeobject1.strftime('%y-%m-%d')
    if (new_format_depart > new_format_arrival):
        messagebox.showinfo("Invalid date", "Arrival date is less than Departure date")
    elif (new_format_depart=="" or new_format_arrival==""):
        messagebox.showerror("Empty", "Please fill the details to update")

    else:
        try:
                    cur.execute(
                        "select is_gate_pass_approved,student_hostel_gate_pass.stud_email from stud_parents_info,student_hostel_gate_pass where stud_parents_info.hostel_gate_pass_id='" + gate_Pass_Id_to_Search + "'" + "AND stud_parents_info.is_gate_pass_approved='Yes' AND student_hostel_gate_pass.hostel_gate_pass_id=stud_parents_info.hostel_gate_pass_id")
                    hostel_id = cur.fetchone();
                    if hostel_id:
                        cur.execute(
                            "Update student_hostel_gate_pass SET departure_date='" + new_format_depart + "'" + " , arrival_date='" + new_format_arrival + "'" + " where student_hostel_gate_pass.hostel_gate_pass_id='" + gate_Pass_Id_to_Search + "'")

                        messagebox.showinfo("Updated", "Your GatePass is updated. Please check your email")
                        sender_email = 'jyotijk1999@gmail.com'
                        sender_password = 'hcicejhgauvieygi'
                        server = smtplib.SMTP('smtp.gmail.com', 587)
                        server.starttls()
                        server.login(sender_email, sender_password)

                        receiaddress = hostel_id[1]

                        email_body = "************************* Hi This is Your Gate Pass *********************" + "\n\n\n" + "Gate Pass ID:" + " " + \
                                     gate_Pass_Id_to_Search + "\n\n\n" + "Name Of the student:" + " " + " " + nm.get() + "\n\n\n" + "Wing:" + " " + wig.get() + "\n\n\n" + "Room Number:" + " " + f'{rm.get()}' + "\n\n\n" + "Departure Date:" + " " + new_format_depart + "\n\n\n" + "Arrival Date:" + " " + new_format_arrival + "\n\n\n" + "\n\n\n\n\n\n\n\n\n\n\n" + "From," + "\n\n\n\n\n" + "JSPM Girls Hostel"
                        message = 'Subject: {}\n\n{}'.format("JSPM Girls Hostel GatePass", email_body)
                        server.sendmail(sender_email, receiaddress, message)
                        messagebox.showinfo("Email", "Send Email")


                        db.commit()
                    else:
                        messagebox.showinfo("Not Possible","Your Gate Pass is  Canceled or Not Approved")
        except Exception as e:

            print(e)
    root.destroy()
    import menuPage

name = Label(root, text=" Name", width=10, bg='#FFFF8F', font=("Calibri", 16))
name.place(x=100, y=140)
nm = Entry(root, width=30, fg='black', border=2, bg="#F5F5DC", font=('Microsoft YaHei UI Light', 11))
nm.config(state=DISABLED)
nm.place(x=130, y=170)

wing = Label(root, text="Wing", width=13, bg='#FFFF8F', font=("Calibri", 16))
wing.place(x=85, y=200)
wig = Entry(root, width=30, fg='black', border=2, bg="#F5F5DC", font=('Microsoft YaHei UI Light', 11))
wig.config(state=DISABLED)
wig.place(x=130, y=230)

room_no = Label(root, text="Room No", width=10, bg='#FFFF8F', font=("Calibri", 16))
room_no.place(x=515, y=200)
rm = Entry(root, width=30, fg='black', border=2, bg="#F5F5DC", font=('Microsoft YaHei UI Light', 11))
rm.config(state=DISABLED)
rm.place(x=530, y=230)

depart = Label(root, text="Departure Date", width=20, bg='#FFFF8F', font=("Calibri", 16))
depart.place(x=90, y=260)
dept = DateEntry(root, width=30, fg='black', border=2, bg="#F5F5DC", font=('Microsoft YaHei UI Light', 11))
dept.config(state=DISABLED)
dept.place(x=130, y=290)

arrival = Label(root, text="Arrival Date", width=20, bg='#FFFF8F', font=("Calibri", 16))
arrival.place(x=470, y=260)
arr = DateEntry(root, width=30, fg='black', border=2, bg="#F5F5DC", font=('Microsoft YaHei UI Light', 11))
arr.config(state=DISABLED)
arr.place(x=530, y=290)

Gate_id = Label(root, text="Gate Pass ID", width=10, bg='#FFFF8F', font=("Calibri", 16))
Gate_id.place(x=520, y=140)
gid = Entry(root, width=30, fg='black', border=2, bg="#F5F5DC", font=('Microsoft YaHei UI Light', 11))
gid.config(state=DISABLED)
gid.place(x=530, y=170)

lb5 = Label(root, text="Do you want to cancel the GatePass?", width=40, bg="#FFFF8F", font=("Calibri", 16))
lb5.place(x=70, y=340)
vars = StringVar()
Radiobutton(root, text="Cancel", padx=5, variable=vars, bg="#FFFF8F", font=("Calibri", 16), value="Cancel",command=cancelentry).place(x=450, y=339)

lb6 = Label(root, text="Do you want to update the GatePass ?", width=40, bg="#FFFF8F", font=("Calibri", 16))
lb6.place(x=70, y=390)
vari = StringVar()
Radiobutton(root, text="Yes", padx=6, variable=vari, bg="#FFFF8F", font=("Calibri", 16), value="Yes",command=yesUpdateEntry).place(x=455, y=390)


    

search = Button(root, width=15, pady=1, text='Search', bg='#93C572', fg='black', font=('Calibri', 12, 'bold'),
           border=2, command=next_page)
search.place(x=530, y=55)

update=Button(root, width=20, pady=5, text='Update', bg='#93C572', fg='black', font=('Calibri', 12, 'bold'),
                 border=2,command=update_GatePass)
update.place(x=360, y=450)
update.config(state=DISABLED)

root.mainloop()