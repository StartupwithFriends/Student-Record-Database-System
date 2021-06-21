"""
    *PROJECT*
    Name - Student Record Manager GUI
    Date - 09/11/2020
    Programming language used - Python3
    Windows Application - Tkinter
    Database Used - MySQL-Python
    Contributors - [ AYUSH NEGI,
                    SHUBH AGGARWAL,
                    AAYUSHI BHANDARI ]
    CBSE project of Class XII for session 2020-2021
                                                    """

# imported modules
import os
from tkinter import *
from tkinter.messagebox import showinfo, showerror
from tkinter.filedialog import askopenfilename
import time
import pandas as pd
import pymysql as MySQLdb
from PIL import ImageTk, Image

"""
Functions created for the project 
1) Create Record 
2) Update Record 
3) Delete Record 
4) Show Record 
5) Search Record 
6) Instructions
7) Main window
"""

"""
Modules needs to be installed
1) pip install pymysql 
2) pip install pandas
3) pip install openpyxl
4) pip install pillow (PIL)
5) pip install cryptography  
"""

"""
Database details -
1) Database Name - studex
2) Table Name - student
3) Field Names = [ Student_Name char(100),
                    Roll_No char(50), 
                    Class char(50),
                    Admission_No char(50),
                    Contact (BIGINT),
                    Mother_Name char(100),
                    Father_Name char(100)]
"""

# Main Code
# Tkinter window
win = Tk()
win.title('Student Record Manager')
width = win.winfo_screenwidth()
height = win.winfo_screenheight()
win.geometry(f'{width}x{height}')
win.iconbitmap(
    'Student Record Database Project\Custom-Icon-Design-Flatastic-7-Student-id.ico')
win.configure(bg='crimson')
win.state('zoomed')

"""
Name : instruction
purpose : makes the instruction page
"""


def instruction():
    global z
    z = Frame(win, bg='crimson')
    z.pack(pady=120)
    lzl = Label(z, text="PLEASE SELECT ANY OPTIONS FROM MENU", font=('Roboto 30 bold underline'), fg='white',
                bg='crimson')
    lzl.pack(pady=40)
    lel = Label(z,
                text="1) CREATE RECORD\n\n2) UPDATE RECORD\n\n3) DELETE RECORD\n\n4) SHOW RECORD\n\n5) SEARCH RECORD",
                font=('Roboto 25 bold'), bg='crimson', fg='white')
    lel.pack()


"""
Name : Create Record
purpose : Appends record to database
"""


def createRecord():
    # global bar
    global z

    """
    Name : call_back
    purpose : retrun back to homescreen
    """

    def call_back():
        try:
            frame3.destroy()
            frame4.destroy()
            frame5.destroy()
            frame6.destroy()
            frame7.destroy()
            frame8.destroy()
            frame9.destroy()
            frame10.destroy()
            frame11.destroy()
            btn2['state'] = NORMAL
            btn3['state'] = NORMAL
            btn4['state'] = NORMAL
            btn5['state'] = NORMAL
            btn6['state'] = NORMAL
        except Exception as e:
            print(e)
        instruction()

    # bar.destroy()
    # lzl.destroy()
    # lel.destroy()
    z.destroy()
    # time.sleep(1)

    frame3 = Frame(win, bg='crimson')
    frame3.pack(side=TOP, pady=80)

    # img = Image.open('Custom-Icon-Design-Flatastic-7-Student-id.ico')
    # ref = img.resize((150, 150), Image.ANTIALIAS)
    # picture = ImageTk.PhotoImage(ref)

    lnl = Button(frame3, text="<==", font=('Roboto 18 bold'), command=call_back, bg='crimson', fg='white',
                 relief='raised')
    lnl.pack(padx=30, side=LEFT, ipadx=30)
    btn7 = Label(frame3, text="PLEASE FILL THE REQUIRED FIELDS", bg='crimson', fg='white', relief='flat',
                 font=('Roboto 30 bold underline'))
    btn7.pack(side=LEFT, pady=5)

    frame4 = Frame(win, bg='crimson')
    frame4.pack(pady=15)
    label2 = Label(frame4, text="Enter Student Name :",
                   bg='crimson', fg='white', font=('Roboto 14 bold'))
    label2.pack(side=LEFT)
    ent1 = Entry(frame4, width=45, relief='solid')
    ent1.pack(side=LEFT, ipady=5)

    frame5 = Frame(win, bg='crimson')
    frame5.pack(pady=15)
    label3 = Label(frame5, text="Enter Roll Number :     ",
                   bg='crimson', fg='white', font=('Roboto 14 bold'))
    label3.pack(side=LEFT)
    ent2 = Entry(frame5, width=45, relief='solid')
    ent2.pack(side=LEFT, ipady=5)

    frame6 = Frame(win, bg='crimson')
    frame6.pack(pady=15)
    label4 = Label(frame6, text="Enter Class/Section : ",
                   bg='crimson', fg='white', font=('Roboto 14 bold'))
    label4.pack(side=LEFT)
    ent3 = Entry(frame6, width=45, relief='solid')
    ent3.pack(side=LEFT, ipady=5)

    frame7 = Frame(win, bg='crimson')
    frame7.pack(pady=15)
    label5 = Label(frame7, text="Enter Admission No : ",
                   bg='crimson', fg='white', font=('Roboto 14 bold'))
    label5.pack(side=LEFT)
    ent4 = Entry(frame7, width=45, relief='solid')
    ent4.pack(side=LEFT, ipady=5)

    frame8 = Frame(win, bg='crimson')
    frame8.pack(pady=15)
    label6 = Label(frame8, text="Enter Contact No :      ",
                   bg='crimson', fg='white', font=('Roboto 14 bold'))
    label6.pack(side=LEFT)
    ent5 = Entry(frame8, width=45, relief='solid')
    ent5.pack(side=LEFT, ipady=5)

    frame9 = Frame(win, bg='crimson')
    frame9.pack(pady=15)
    label7 = Label(frame9, text="Enter Mother's Name :",
                   bg='crimson', fg='white', font=('Roboto 14 bold'))
    label7.pack(side=LEFT)
    ent6 = Entry(frame9, width=45, relief='solid')
    ent6.pack(side=LEFT, ipady=5)

    frame10 = Frame(win, bg='crimson')
    frame10.pack(pady=15)
    label8 = Label(frame10, text="Enter Father's Name : ",
                   bg='crimson', fg='white', font=('Roboto 14 bold'))
    label8.pack(side=LEFT)
    ent7 = Entry(frame10, width=45, relief='solid')
    ent7.pack(side=LEFT, ipady=5)

    # Name : clear_all
    # purpose : clears all the entry field
    def clear_all():
        ent1.delete(0, "end")
        ent2.delete(0, "end")
        ent3.delete(0, "end")
        ent4.delete(0, "end")
        ent5.delete(0, "end")
        ent6.delete(0, "end")
        ent7.delete(0, "end")

    # Name : Submit
    # purpose : save all records to database
    def submit():
        # Making connection to the MYSQLdb server
        db = MySQLdb.connect('localhost', 'root', 'ayush256', 'studex')
        cursor = db.cursor()

        # rows
        Student_Name = []
        Roll_No = []
        Class = []
        Admission_No = []
        Contact = []
        Mother_Name = []
        Father_Name = []

        Studname = str(ent1.get())
        Student_Name.append(Studname)
        roll = str(ent2.get())
        Roll_No.append(roll)
        classname = str(ent3.get())
        Class.append(classname)
        admission = str(ent4.get())
        Admission_No.append(admission)
        contact = str(ent5.get())
        Contact.append(contact)
        mother = str(ent6.get())
        Mother_Name.append(mother)
        father = str(ent7.get())
        Father_Name.append(father)

        # types of fields
        person = [(Student_Name, Roll_No, Class, Admission_No,
                   Contact, Mother_Name, Father_Name)]

        try:
            if Studname == "" or roll == "" or classname == "" or admission == "" or contact == "" or mother == "" or \
                    father == "":
                showerror("Empty Fields", "All fields are necessary")
            else:
                # sqlFormula
                sqlFormula = "INSERT INTO student (Student_Name, Roll_No, Class, Admission_No, Contact, Mother_Name, " \
                             "Father_Name) VALUES (%s, %s, %s, %s, %s, %s, %s) "

                # executing new data
                cursor.executemany(sqlFormula, person)

                # commit the changes
                db.commit()

                # success message
                showinfo("Done", "Record Saved Successfully")

        except:

            formula = "CREATE DATABASE studex"
            cursor.execute(formula)
            formula1 = "CREATE TABLE student(Student_Name char(100), Roll_No char(50), Class char(50), Admission_No " \
                       "char(50), Contact BIGINT, Mother_Name char(100), Father_Name char(100) "
            cursor.execute(formula1)

            # sqlFormula
            sqlFormula = "INSERT INTO student (Student_Name, Roll_No, Class, Admission_No, Contact, Mother_Name, " \
                         "Father_Name) VALUES (%s, %s, %s, %s, %s, %s, %s) "

            # executing new data
            cursor.executemany(sqlFormula, person)

            # commit the changes
            db.commit()

            # success message
            showinfo("Done", "Record Saved Successfully")

    frame11 = Frame(win, bg='crimson')
    frame11.pack(pady=15)

    sub = Button(frame11, text="Submit", bg='orange', fg='white',
                 font=('Roboto 12 bold'), command=submit)
    sub.pack(ipadx=68, ipady=5, pady=20)
    clr = Button(frame11, text='Clear', bg='orange', fg='white',
                 font=('Roboto 12 bold'), command=clear_all)
    clr.pack(pady=10, ipadx=72, ipady=5)

    btn2['state'] = DISABLED
    btn3['state'] = DISABLED
    btn4['state'] = DISABLED
    btn5['state'] = DISABLED
    btn6['state'] = DISABLED


"""
Name : updateRecord
purpose : updates the record in database
"""


def updateRecord():
    global bar
    global z
    z.destroy()
    # time.sleep(1)

    """
    Name : call_back1
    purpose : retrun back to homescreen
    """

    def call_back1():
        try:
            bar.destroy()
            btn2['state'] = NORMAL
            btn3['state'] = NORMAL
            btn4['state'] = NORMAL
            btn5['state'] = NORMAL
            btn6['state'] = NORMAL
        except Exception as e:
            print(e)
        instruction()

    # clears the hintText
    def on_first_click(event):
        fastback = True
        if fastback:
            entry.delete(0, "end")

    # clears the hintText
    def on_second_click(event):
        secondly = True
        if secondly:
            entry1.delete(0, 'end')

    # lzl.destroy()
    # lel.destroy()
    # time.sleep(1)

    def changeRecord():
        # global bar

        db = MySQLdb.connect('localhost', 'root', 'ayush256', 'studex')
        cursor = db.cursor()
        cursor1 = db.cursor()

        a = var.get()  # the value to be changed
        b = var1.get()  # to find the value by category
        c = entry1.get()  # new value
        d = entry.get()  # the value to change

        try:
            if c == "" or d == "":
                showerror("Empty field", "All fields are necessary")
            else:
                cursor.execute(
                    f'UPDATE student SET {a} = "{c}" where {b} = "{d}"')
                showinfo('Done', 'Record Updated Successfully')
                db.commit()
        except Exception as e:
            showerror("Error", f"{e}")

        cursor1.execute(f"SELECT * FROM student where {a} = '{d}'")

        # logs = []
        #
        # for i in cursor1:
        #     logs.append(i)
        # print(logs)

    bar = Frame(win, bg='crimson')
    bar.pack(pady=80)

    lnl = Button(bar, text="<==", font=('Roboto 18 bold'), command=call_back1, bg='crimson', fg='white',
                 relief='raised')
    lnl.pack(padx=30, side=TOP, ipadx=30)

    lrl = Label(bar, text='PLEASE SELECT THE FIELD TO UPDATE', font=('Roboto 25 bold underline'), bg='crimson',
                fg='white')
    lrl.pack(pady=10)

    var = StringVar(bar)
    var.set("Student_Name")  # initial value

    option = OptionMenu(bar, var, "Student_Name", "Roll_No", "Class", "Admission_No", "Contact", "Mother_Name",
                        "Father_Name")
    option.pack(ipadx=150, ipady=20, pady=40)

    lrl = Label(bar, text='PLEASE SELECT THE FIELD TO FIND BY', font=('Roboto 25 bold underline'), bg='crimson',
                fg='white')
    lrl.pack(pady=10)

    var1 = StringVar(bar)
    var1.set("Student_Name")  # initial value

    option1 = OptionMenu(bar, var1, "Student_Name", "Roll_No", "Class", "Admission_No", "Contact", "Mother_Name",
                         "Father_Name")
    option1.pack(ipadx=150, ipady=20, pady=40)

    entry = Entry(bar, width=50, font=('Roboto 12 bold'), relief='solid')
    entry.insert(0, "Enter the value to find by...")
    entry.bind('<FocusIn>', on_first_click)
    entry.pack(ipadx=40, pady=50, ipady=12)

    entry1 = Entry(bar, width=50, font=('Roboto 12 bold'), relief='solid')
    entry1.insert(0, "Enter the new value...")
    entry1.bind('<FocusIn>', on_second_click)
    entry1.pack(ipadx=50, pady=20, ipady=12)

    button = Button(bar, text="Update", command=changeRecord, bg='blue', fg='white', font=('Roboto 15 bold'),
                    relief='raised')
    button.pack(ipadx=100, ipady=8, pady=20)

    btn2['state'] = DISABLED
    btn3['state'] = DISABLED
    btn4['state'] = DISABLED
    btn5['state'] = DISABLED
    btn6['state'] = DISABLED


"""
Name : deleteRecord
purpose : Delete record from the database
"""


# to solve multiple deletion of code
# if multiple records have same value
def deleteRecord():
    global z
    global baz
    z.destroy()
    # time.sleep(1)
    db = MySQLdb.connect('localhost', 'root', 'ayush256', 'studex')
    cursor = db.cursor()

    # clears the hintText
    def on_third_click(event):
        thirdly = True
        if thirdly:
            entry2.delete(0, 'end')

    """
    Name : call_back2
    purpose : retrun back to homescreen
    """

    def call_back2():
        try:
            baz.destroy()
            btn2['state'] = NORMAL
            btn3['state'] = NORMAL
            btn4['state'] = NORMAL
            btn5['state'] = NORMAL
            btn6['state'] = NORMAL
        except Exception as e:
            print(e)
        instruction()

    baz = Frame(win, bg='crimson')
    baz.pack(pady=80)

    lnl = Button(baz, text="<==", font=('Roboto 18 bold'), command=call_back2, bg='crimson', fg='white',
                 relief='raised')
    lnl.pack(padx=30, side=TOP, ipadx=30)

    lKl = Label(baz, text='PLEASE SELECT THE FIELD TO IDENTIFY RECORD', font=('Roboto 25 bold underline'), bg='crimson',
                fg='white')
    lKl.pack(pady=10)

    vaz = StringVar(baz)
    vaz.set("Student_Name")  # initial value

    options = OptionMenu(baz, vaz, "Student_Name", "Roll_No", "Class", "Admission_No", "Contact", "Mother_Name",
                         "Father_Name")
    options.pack(ipadx=150, ipady=20, pady=40)

    entry2 = Entry(baz, width=50, font=('Roboto 12 bold'), relief='solid')
    entry2.insert(0, "Enter the value to find by...")
    entry2.bind('<FocusIn>', on_third_click)
    entry2.pack(ipadx=40, pady=50, ipady=12)

    def del_rec():

        m = vaz.get()
        n = entry2.get()

        try:
            if n == "":
                showerror("Empty Field", "All fields are neccessary")
            else:
                cursor.execute(f"DELETE FROM student where {m} = '{n}'")
                db.commit()
                showinfo('Done', "Record is deleted successfully")
        except Exception as e:
            showerror("Error", f"{e}")

    button = Button(baz, text="Delete", command=del_rec, bg='blue', fg='white', font=('Roboto 15 bold'),
                    relief='raised')
    button.pack(ipadx=100, ipady=8, pady=20)

    btn2['state'] = DISABLED
    btn3['state'] = DISABLED
    btn4['state'] = DISABLED
    btn5['state'] = DISABLED
    btn6['state'] = DISABLED


def searchRecord():
    global z
    global bac
    z.destroy()
    # time.sleep(1)

    db = MySQLdb.connect('localhost', 'root', 'ayush256', 'studex')
    cursor1 = db.cursor()

    """
    Name : call_back3
    purpose : retrun back to homescreen
    """

    def call_back3():
        try:
            bac.destroy()
            btn2['state'] = NORMAL
            btn3['state'] = NORMAL
            btn4['state'] = NORMAL
            btn5['state'] = NORMAL
            btn6['state'] = NORMAL
        except Exception as e:
            print(e)
        instruction()

    # clears the hintText
    def on_forth_click(event):
        forthclick = True
        if forthclick:
            forthclick = False
            entry3.delete(0, 'end')

    bac = Frame(win, bg='crimson')
    bac.pack(pady=80)

    lnl = Button(bac, text="<==", font=('Roboto 18 bold'), command=call_back3, bg='crimson', fg='white',
                 relief='raised')
    lnl.pack(padx=30, side=TOP, ipadx=30)

    lvl = Label(bac, text='PLEASE SELECT THE FIELD TO IDENTIFY RECORD', font=('Roboto 25 bold underline'), bg='crimson',
                fg='white')
    lvl.pack(pady=10)

    vaf = StringVar(bac)
    vaf.set("Student_Name")  # initial value

    optionz = OptionMenu(bac, vaf, "Student_Name", "Roll_No", "Class", "Admission_No", "Contact", "Mother_Name",
                         "Father_Name")
    optionz.pack(ipadx=150, ipady=20, pady=40)

    entry3 = Entry(bac, width=50, font=('Roboto 12 bold'), relief='solid')
    entry3.insert(0, "Enter the value to find by...")
    entry3.bind('<FocusIn>', on_forth_click)
    entry3.pack(ipadx=40, pady=50, ipady=12)

    '''
    Name : search_rec
    purpose : search the required info and return the output
    '''

    def search_rec():
        x = vaf.get()
        y = entry3.get()

        eight = []

        if y == "":
            showerror("Empty field", "All fields are necessary")
        else:
            cursor1.execute(f"SELECT * FROM student where {x} = '{y}'")

        for i in cursor1:
            eight.append(i)

        if len(eight) == 0:
            showinfo("Sorry", "No result found")
        else:
            search_info = []

            for i in eight:
                search_info.append({'Student Name': i[0], 'Roll Number': i[1], 'Class': i[2], 'Admission Number': i[3],
                                    'Contact': i[4], "Mother's Name": i[5], "Father's Name": i[6]})

            df1 = pd.DataFrame(search_info)

            df1.to_excel('search_record.xlsx', sheet_name='Sheet2')

            showinfo("Wait", "File is Opening")

            os.startfile('search_record.xlsx')

    button = Button(bac, text="Search", command=search_rec, bg='blue', fg='white', font=('Roboto 15 bold'),
                    relief='raised')
    button.pack(ipadx=100, ipady=8, pady=20)

    btn2['state'] = DISABLED
    btn3['state'] = DISABLED
    btn4['state'] = DISABLED
    btn5['state'] = DISABLED
    btn6['state'] = DISABLED


"""
Name : showRecord
purpose : show record in the database
"""


def showRecord():
    """
    Student_Name = []
    Roll_No = []
    Class = []
    Admission_No = []
    Contact = []
    Mother_Name = []
    Father_Name = []
    """

    one = []
    two = []
    three = []
    four = []
    five = []
    six = []
    seven = []

    db = MySQLdb.connect('localhost', 'root', 'ayush256', 'studex')
    cursor = db.cursor()

    cursor.execute(
        "SELECT Student_Name from student order by Student_Name ASC")

    for i in cursor:
        one.append(i)

    cursor.execute("SELECT Roll_No from student order by Student_Name ASC")

    for j in cursor:
        two.append(j)

    cursor.execute("SELECT Class from student order by Student_Name ASC")

    for k in cursor:
        three.append(k)

    cursor.execute(
        "SELECT Admission_No from student order by Student_Name ASC")

    for e in cursor:
        four.append(e)

    cursor.execute("SELECT Contact from student order by Student_Name ASC")

    for _ in cursor:
        five.append(_)

    cursor.execute("SELECT Mother_Name from student order by Student_Name ASC")

    for a in cursor:
        six.append(a)

    cursor.execute("SELECT Father_Name from student order by Student_Name ASC")

    for b in cursor:
        seven.append(b)

    # All info is stored here
    final_info = []

    try:

        for i, j, k, l, m, n, p in zip(one, two, three, four, five, six, seven):
            final_info.append({'Student Name': i, 'Roll Number': j, 'Class': k, 'Admission Number': l, 'Contact': m,
                               "Mother's Name": n, "Father's Name": p})

        df = pd.DataFrame(final_info)

        df.to_excel('student_record.xlsx', sheet_name='Sheet1')

        showinfo("Wait", "File is Opening")

        try:
            os.startfile('student_record.xlsx')
        except Exception as e:
            a = askopenfilename()
            print(e)

    except Exception as e:
        showerror("Error", f"{e}")


"""
Name : main_window
purpose : Navigates to the main window
"""


def main_window():
    global lbl1, lbl, btn1, btn2, btn3, btn4, btn5, btn6, z
    # Destroy frame2 by clicking "CONTINUE" button
    frame2.destroy()
    time.sleep(1)

    instruction()

    # Buttons are set to NORMAL OR ACTIVE STATE
    btn2['state'] = NORMAL
    btn3['state'] = NORMAL
    btn4['state'] = NORMAL
    btn5['state'] = NORMAL
    btn6['state'] = NORMAL


# side panel
sideFrame = Frame(win, bg='orange')
sideFrame.pack(side=LEFT, fill=Y, ipadx=80)
# buttons inside the sideFrame
lol = Label(sideFrame, text="MENU", bg='orange', fg='white',
            relief='raised', font=('Roboto 25 bold'))
lol.pack(side=TOP, ipady=30, fill=X)
btn2 = Button(sideFrame, text="Create Record", relief="raised", bg='white', font=('Roboto 15 bold'),
              command=createRecord)
btn2.pack(side=TOP, pady=50, ipady=18, ipadx=75)
btn2['state'] = DISABLED  # set current button state to DISABLED
btn3 = Button(sideFrame, text="Update Record", relief="raised", bg='white', font=('Roboto 15 bold'),
              command=updateRecord)
btn3.pack(side=TOP, pady=50, ipady=18, ipadx=75)
btn3['state'] = DISABLED  # set current button state to DISABLED
btn4 = Button(sideFrame, text="Delete Record", relief="raised", bg='white', font=('Roboto 15 bold'),
              command=deleteRecord)
btn4.pack(side=TOP, pady=50, ipady=18, ipadx=75)
btn4['state'] = DISABLED  # set current button state to DISABLED
btn5 = Button(sideFrame, text="Show Record", relief="raised",
              bg='white', font=('Roboto 15 bold'), command=showRecord)
btn5.pack(side=TOP, pady=50, ipady=18, ipadx=75)
btn5['state'] = DISABLED  # set current button state to DISABLED
btn6 = Button(sideFrame, text="Search Record", relief="raised", bg='white', font=('Roboto 15 bold'),
              command=searchRecord)
btn6.pack(side=TOP, pady=50, ipady=18, ipadx=75)
btn6['state'] = DISABLED  # set current button state to DISABLED

# frame2 / Centre frame
frame2 = Frame(win, bg="crimson")
frame2.pack(side=TOP, pady=100)
# widgets of frame2
image = Image.open(
    'Student Record Database Project\Custom-Icon-Design-Flatastic-7-Student-id.ico')
resized = image.resize((250, 250), Image.ANTIALIAS)
new_pic = ImageTk.PhotoImage(resized)
lbl = Label(frame2, text="WELCOME\nTO\nSTUDENT RECORD MANAGER ", bg="crimson", fg='white',
            font=('Roboto 35 bold underline'))
lbl.pack(pady=20)
lbl1 = Label(frame2, image=new_pic, bg="crimson", relief="flat")
lbl1.pack(pady=30)
btn1 = Button(frame2, text='CONTINUE', fg='white', bg='blue',
              font=('Roboto 12 bold'), command=main_window)
btn1.pack(pady=50, ipady=15, ipadx=70)

# This is the bottom frame
btmFrame = Frame(win, bg='orange')
btmFrame.pack(side=BOTTOM, fill=X, ipady=2)
# creators of project name
lbl1 = Label(btmFrame, text='© Created by AYUSH NEGI, SHUBH AGGARWAL, AAYUSHI BHANDARI (2020-2021)', bg='orange',
             fg='white', font=('TimesNewRoman 13 bold'))
lbl1.pack()

win.mainloop()
