from tkinter import *
import pymongo
from tkinter import messagebox
# Table class
def add_user(data):
    messagebox.showinfo("Invaild",data)
class Table:
    # Initialize a constructor
    def __init__(self, gui):
        # An approach for creating the table
        global i 
        global j
        for employee_listv in employee_list:
            print(employee_listv)
            j=0
            employee_listvaslist=list(employee_listv.values())
            for emp in employee_listvaslist:
                print(emp)
                if employee_listvaslist[0]==emp:
                        self.entry = Entry(gui, width=20, bg='LightSteelBlue',fg='Black',
                                       font=('Arial', 16, 'bold'))
                else:
                   self.entry =Entry(gui, width=20, fg='blue',border=5,
                               font=('Arial', 16, ''))
                   self.entry.grid(row=i, column=j)     
                   self.entry.insert(END,emp)
                if employee_listvaslist[-1]==emp:
                   self.button=Button(gui, text='Submit' , width=20,bg="green",fg='white').grid(row=i, column=j+1)
                j=j+1

            i=i+1
myclient=pymongo.MongoClient("mongodb://localhost")
my_db=myclient["mini-project"]
my_coll=my_db["ebs"]
employee_list=my_coll.find({"status":"true"},{'uname',"oldunit"})
print(type(employee_list))
# take the data
"""employee_list = [('ID', 'Name', 'City', 'Age'),
        (1, 'Gorge', 'California', 30),
       (2, 'Maria', 'New York', 19),
       (3, 'Albert', 'Berlin', 22),
       (4, 'Harry', 'Chicago', 19),
       (5, 'Vanessa', 'Boston', 31),
       (6, 'Ali', 'Karachi', 30)]
"""
# find total number of rows and
# columns in list
j=0
i=5
# create root window
gui = Tk()
table = Table(gui)
# Table class
def add_user(data):
    messagebox.showinfo("Invaild",data)
class Table:
    # Initialize a constructor
    def __init__(self, gui):
        # An approach for creating the table
        global i 
        global j
        for employee_listv in employee_list:
            print(employee_listv)
            j=0
            employee_listvaslist=list(employee_listv.values())
            for emp in employee_listvaslist:
                print(emp)
                if employee_listvaslist[0]==emp:
                        self.entry = Entry(gui, width=20, bg='LightSteelBlue',fg='Black',
                                       font=('Arial', 16, 'bold'))
                else:
                   self.entry =Entry(gui, width=20, fg='blue',border=5,
                               font=('Arial', 16, ''))
                   self.entry.grid(row=i, column=j)     
                   self.entry.insert(END,emp)
                if employee_listvaslist[-1]==emp:
                   self.button=Button(gui, text='Submit' , width=20,bg="green",fg='white').grid(row=i, column=j+1)
                j=j+1

            i=i+1
myclient=pymongo.MongoClient("mongodb://localhost")
my_db=myclient["mini-project"]
my_coll=my_db["ebs"]
employee_list=my_coll.find({"status":"true"},{'uname',"oldunit"})
print(type(employee_list))
# take the data
"""employee_list = [('ID', 'Name', 'City', 'Age'),
        (1, 'Gorge', 'California', 30),
       (2, 'Maria', 'New York', 19),
       (3, 'Albert', 'Berlin', 22),
       (4, 'Harry', 'Chicago', 19),
       (5, 'Vanessa', 'Boston', 31),
       (6, 'Ali', 'Karachi', 30)]
"""
# find total number of rows and
# columns in list
j=0
i=5
# create root window
gui = Tk()
table = Table(gui)
gui.mainloop()