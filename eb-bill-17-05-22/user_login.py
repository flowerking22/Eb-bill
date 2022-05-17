from tkinter import *
from functools import partial
import pymongo
myclient=pymongo.MongoClient("mongodb://localhost")
my_db=myclient["mini-project"]
my_coll=my_db["ebs"]


#window
root = Tk()  
root.geometry('400x150')  
root.title('Tkinter Login Form - pythonexamples.org')

#username label and text entry box
usernameLabel = Label( root, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry( root, textvariable=username).grid(row=0, column=1)  

#password label and password entry box
passwordLabel = Label( root,text="Password").grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry( root, textvariable=password, show='*').grid(row=1, column=1)  


result=""

print("username entered :", username.get())
print("password entered :", password.get())
#login button
def result_fun(result):
    for inn in result:
        print(inn)
def validateLogin():
    print("username entered :", username.get())
    print("password entered :", password.get())
    result=my_coll.find({"uname":username.get()},{'uname',"oldunit"})
    result_fun(result)
Button( root, text="Login", command=validateLogin).grid(row=4, column=0)  
def user_registration():
    root.destroy()
    import user_registration

def adminPage():
    root.destroy()
    import admin
Button(root, text='adminPage' , width=20,bg="black",fg='white',command=adminPage).grid(row=5, column=0)
Button(root, text='user_registration' , width=20,bg="black",fg='white',command=user_registration).grid(row=6, column=0)
root.mainloop()