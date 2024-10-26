# Importing required libraries
import mysql.connector

# Establishing database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="helloworld@123"
)

# Creating a cursor object
cursor = db.cursor()

# SQL queries to create tables
student_table = """
CREATE TABLE IF NOT EXISTS student ( 
    ID INT(5) PRIMARY KEY,
    Name VARCHAR(30),
    E_Name VARCHAR(30),
    Age INT(2),
    DOB DATE,
    Stream VARCHAR(10),
    marks VARCHAR(03),
    Fee INT(10),
    Address VARCHAR(30)
)
"""

tutor_table = """
CREATE TABLE IF NOT EXISTS tutor (
    ID INT(5) PRIMARY KEY,
    Name VARCHAR(30),
    Course VARCHAR(20),
    Phone VARCHAR(15),
    DOJ DATE,
    Salary INT(10),
    Age INT(2),
    Address VARCHAR(30)
)
"""

routine_table = """
CREATE TABLE IF NOT EXISTS routine (
    Day VARCHAR(10) PRIMARY KEY,
    Stream VARCHAR(30),
    `400pm_430pm` VARCHAR(20),
    `440pm_510pm` VARCHAR(20),
    `520pm_550pm` VARCHAR(20),
    `600pm_630pm` VARCHAR(20)
)
"""

# Check if the database exists and create if not
cursor.execute("SHOW DATABASES")
databases = cursor.fetchall()

if ('coaching_centre',) not in databases:
    cursor.execute("CREATE DATABASE coaching_centre")
    print("Database 'coaching_centre' created.")

cursor.execute("USE coaching_centre")

# Check and create tables if they do not exist
cursor.execute("SHOW TABLES")
tables = cursor.fetchall()

if ('student',) not in tables:
    cursor.execute(student_table)
    print("Table 'student' created.")
if ('tutor',) not in tables:
    cursor.execute(tutor_table)
    print("Table 'tutor' created.")
if ('routine',) not in tables:
    cursor.execute(routine_table)
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
    for day in days:
        cursor.execute(f"INSERT INTO routine (Day) VALUES ('{day}')")
        db.commit()
    print("Table 'routine' created.")

# Function definitions
def admin(a):
    if a == '1':
        search = input("Enter search option 1:courses 2:tutor 3:student 4:age 5:salary 6:fee 7:marks 8:dob 9:doj :: ")
        if search == '1':
            cursor.execute("SELECT course FROM tutor")
            print("(courses)")
        elif search == '2':
            cursor.execute("SELECT ID , Name FROM tutor")
            print("(ID , Name)")
        elif search == '3':
            cursor.execute("SELECT ID , Name FROM student")
            print("(ID , Name)")
        elif search == '4':
            who = input("enter 1:student 2:teacher :: ")
            if (who == '1'):
                cursor.execute("SELECT ID , Age FROM student" )
                print("(ID , Age)")
            elif (who == '2'):
                cursor.execute("SELECT ID , Age FROM tutor" )
                print("(ID , Age)")
            else:
                admin(a)
        elif search == '5':
            cursor.execute("SELECT ID , Salary FROM tutor" )
            print("(ID , Salary)")
        elif search == '6':
           cursor.execute("SELECT ID , Fee FROM student" )
           print("(ID , Fee)")
        elif search == '7':
           cursor.execute("SELECT ID , Marks FROM student" )
           print("(ID , Marks)")
        elif search == '8':
           cursor.execute("SELECT ID , DOB FROM student" )
           print("(ID , DOB)")
        elif search == '9':
           cursor.execute("SELECT ID , DOJ FROM tutor" )
           print("(ID , DOJ)")
        else:
            print("invalid input")
            admin(a)
        result = cursor.fetchall()
        for row in result:
                print(row)
    elif a == '2':
        option = input("Enter 1:Student 2:Tutor :: ")
        if option == '1':
            sid = input("Enter student ID: ")
            sname = input("Enter student name: ")
            sage = input("Enter student age: ")
            sdob = input("Enter student date of birth (YYYY-MM-DD): ")
            smarks = input("Enter student marks: ")
            sstream = input("Enter student stream: ")
            sfee = input("Enter student fee: ")
            saddress = input("Enter student address: ")
            cursor.execute(
                "INSERT INTO student (ID, Name, Age, DOB, Stream, Fee, Address, marks) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                (sid, sname, sage, sdob, sstream, sfee, saddress, smarks)
            )
            db.commit()
            print("Student record added.")
        elif option == '2':
            tid = input("Enter tutor ID: ")
            tname = input("Enter tutor name: ")
            tcourse = input("Enter tutor course: ")
            tphone = input("Enter tutor phone number: ")
            tdob = input("Enter tutor DOJ (YYYY-MM-DD): ")
            tsalary = input("Enter tutor salary: ")
            tage = input("Enter tutor age: ")
            taddress = input("Enter tutor address: ")
            cursor.execute(
                "INSERT INTO tutor (ID, Name, Course, Phone, DOJ, Salary, Age, Address) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                (tid, tname, tcourse, tphone, tdob, tsalary, tage, taddress)
            )
            db.commit()
            print("Tutor record added.")
        else:
            print("Invalid input.")
            admin(a)
    elif a == '3':
        option = input("Enter 1:Student  2: Tutor :: ")
        if option == '1':
            sid = input("Enter student ID: ")
            cursor.execute("SELECT ID FROM student")
            students = cursor.fetchall()
            present = 0
            for student in students:
                if student[0] == int(sid):
                    present = 1
                    break
            if(present == 0):
                print("Student record not present.")
            else:
                cursor.execute("DELETE FROM student WHERE ID = %s", (sid,))
                db.commit()
                print("Student record deleted.")
        elif option == '2':
            tid = input("Enter tutor ID: ")
            cursor.execute("SELECT * FROM student")
            tutors = cursor.fetchall()
            present = 0
            for tutor in tutors:
                if tutor[0] == int(tid):
                    present = 1
                    break
            if(present == 0):
                print("Tutor record not present.")
            else:
                cursor.execute("DELETE FROM tutor WHERE ID = %s", (tid,))
                db.commit()
                print("tutor record deleted.")
        else:
            print("Invalid input.")
            admin(a)
    elif a == '4':
        option = input("Enter 1:To change routine 2:To change student record 3:To change Tutor record :: ")

        if option == '1':
            rday = input("Enter day on which to update record: ")
            rchange = input("Enter routine property: stream , 400pm_430pm , 440pm_510pm , 520pm_550pm , 600pm_630pm : ")
            rchanged = input("Enter new value : ")
            cursor.execute(f"UPDATE routine set {rchange} = '{rchanged}' WHERE day = '{rday}'" )
            db.commit()
            print("Routine updated.")
        elif option == '2':
            sid = input("Enter student ID to update record: ")
            schange = input("Enter student property: name,e_name,age,dob,stream,fee,address to update record: ")
            schanged = input("Enter new value : ")
            cursor.execute(f"UPDATE student set {schange} = '{schanged}' WHERE ID = '{sid}'")
            db.commit()
            print("Student record updated.")
        elif option == '3':
            tid = input("Enter Tutor ID to update record: ")
            tchange = input("Enter Tutor property: stream , fee , address to update record: ")
            tchanged = input("Enter new value : ")
            cursor.execute(f"UPDATE tutor set {tchange} = '{tchanged}' WHERE ID = '{tid}'")
            db.commit()
            print("Tutor record updated.")
        else:
            print("Invalid input.")
            admin(a)

def tutor(b):
    if b == '1':
        option = input("1: student detail 2:salary :: ")
        if(option == '1'):
            sid = input("Enter student ID: ")
            cursor.execute("SELECT Name , Stream , marks FROM student WHERE ID = %s", (sid,))
            print(f"Name , Stream , marks of ID {sid}")
        elif option == '2':
            tid = input("Enter teacher ID: ")
            cursor.execute("SELECT Salary FROM Tutor WHERE ID = %s",(tid,))
            print("(Salary of ID {tid})")
        else:
            print("invalid input")
            tutor(b)
    elif b == '2':
        day = input("Enter the day: ")
        cursor.execute("SELECT * FROM routine WHERE Day = %s", (day,))
        print(f"Routine for the {day}")
    else:
        print("Invalid input.")
        return
    result = cursor.fetchall()
    for item in result:
        print(item)

def student(c):
    if c=='1':
        option = input("Enter 1:Marks 2:Fees 3:Name of teachers :: ")
        if option == '1':
            sid = input("Enter student ID : ")
            cursor.execute("Select marks from student where ID = %s" , (sid,))
            print("(Marks)")
        elif option == '2':
            sid = input("Enter student ID : ")
            cursor.execute("Select Fee from student where ID = %s" , (sid,))
            print("(Fee)")
        elif option == '3':
            cursor.execute("Select Name,course from tutor")
            print("(Name , Course)")
        else:
            print("invalid input")
            student(c)
    elif c=='2':
        stream = input("Enter stream : ")
        cursor.execute("SELECT * from routine WHERE Stream = %s" , (stream,))
        print(f"Routine for the {stream}")
    else:
        print("Invalid input.")
        return

    result = cursor.fetchall()
    for item in result:
        print(item)

def run():
    user = input("ENTER YOUR ROLE (ADMIN, TUTOR, STUDENT) or q to exit ::  ").lower()

    if user == "admin":
        a = input("""
            Enter 1: Search
            Enter 2: Add/Insert
            Enter 3: Delete
            Enter 4: Update
        """)
        admin(a)
    elif user == "tutor":
        b = input("""
            Enter 1: Search
            Enter 2: Check Routine
        """)
        tutor(b)
    elif user == "student":
        c = input("""
            Enter 1: Search
            Enter 2: Check Routine
        """)
        student(c)
    elif user == "q":
        # Disconnecting from the server
        db.close()
        print("Disconnected from the database.")
        return
    else:
        print("No options available.")
    run()
# Run the application
run()