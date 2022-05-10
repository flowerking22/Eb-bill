from tkinter import *
from tkinter import messagebox

#Creating object 'root' of Tk()
root = Tk()

#Providing Geometry to the form
root.geometry("500x500")

#Providing title to the form
root.title('Registration form')

#this creates 'Label' widget for Registration Form and uses place() method.
label_0 =Label(root,text="Registration form", width=20,font=("bold",20),bg="red",)
#place method in tkinter is  geometry manager it is used to organize widgets by placing them in specific position
label_0.place(x=90,y=60)

#this creates 'Label' widget for Fullname and uses place() method.
label_1 =Label(root,text="FullName", width=20,font=("bold",10))
fullname = StringVar()
label_1.place(x=80,y=130)

#this will accept the input string text from the user.
entry_1=Entry(root,textvariable=fullname)
entry_1.place(x=240,y=130)
# 2 password
label_2 =Label(root,text="Password", width=20,font=("bold",10))
label_2.place(x=90,y=150)

#this will accept the input string text from the user.
entry_2=Entry(root,show="*")
entry_2.place(x=240,y=150)

#this creates 'Label' widget for Email and uses place() method.
label_3 =Label(root,text="Email", width=20,font=("bold",10))
label_3.place(x=68,y=180)

entry_3=Entry(root)
entry_3.place(x=240,y=180)

#this creates 'Label' widget for Gender and uses place() method.
label_4 =Label(root,text="Property Type:", width=20,font=("bold",10))
label_4.place(x=70,y=230)


#the variable 'var' mentioned here holds Integer Value, by deault 0
var=IntVar()

#this creates 'Radio button' widget and uses place() method
Radiobutton(root,text="House",padx= 5, variable= var, value=1).place(x=235,y=230)
Radiobutton(root,text="Industriy",padx= 20, variable= var, value=2).place(x=290,y=230)


##this creates 'Label' widget for country and uses place() method.
label_5=Label(root,text="State",width=20,font=("bold",10))
label_5.place(x=70,y=280)

#this creates list of countries available in the dropdownlist.
list_of_country=["Tamilnadu","Karnataka","Kerala"]

#the variable 'c' mentioned here holds String Value, by default ""
c=StringVar()
droplist=OptionMenu(root,c, *list_of_country)
droplist.config(width=15)
c.set('Select your Country')
droplist.place(x=240,y=280)

def alert():
    print("alert")
    if fullname.get() != "":        
        return  messagebox.showinfo("Message",fullname.get()+"  Register Successfully")
         
    messagebox.showinfo("Invaild","  All The Details Required To Register")
    
#this creates button for submitting the details provides by the user
Button(root, text='Register' , width=20,bg="black",fg='white',command=alert).place(x=180,y=380)
def prevPage():
    root.destroy()
    import login


Button(
    root, 
    text="Next Page", 
    command=prevPage
    ).pack(fill=X, expand=TRUE, side=LEFT)


#this will run the mainloop.
root.mainloop()
