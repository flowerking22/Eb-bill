from tkinter import *
from tkinter import messagebox
import pymongo
import sys
from dbconfig import DBINFORM
dbobj=DBINFORM()
#Creating object 'root' of Tk()
root = Tk() 
#Providing Geometry to the form
root.geometry("500x500")
# Variable Declartion In User_Registration
username=StringVar()
password=StringVar()
user_type=StringVar()
state=StringVar()

#Providing title to the form
root.title('User Registration form')
root.bg="black"
#this creates 'Label' widget for Registration Form and uses place() method.
label_0 =Label(root,text="Add User", width=20,font=("bold",20),bg="black",fg="white")
#place method in tkinter is  geometry manager it is used to organize widgets by placing them in specific position
label_0.place(x=90,y=60)

#this creates 'Label' widget for Fullname and uses place() method.
label_1 =Label(root,text="UserName:-", width=20,font=("bold",10))
label_1.place(x=80,y=130)

#this will accept the input string text from the user.
entry_1=Entry(root,textvariable=username)
entry_1.place(x=240,y=130)

#this creates 'Label' widget for Email and uses place() method.
label_3 =Label(root,text="Password", width=20,font=("bold",10))
label_3.place(x=68,y=180)

entry_3=Entry(root,show="*",textvariable=password)
entry_3.place(x=240,y=180)

#this creates 'Label' widget for Gender and uses place() method.
label_4 =Label(root,text="User_type", width=20,font=("bold",10))
label_4.place(x=70,y=230)


#the variable 'var' mentioned here holds Integer Value, by deault 0

#this creates 'Radio button' widget and uses place() method
Radiobutton(root,text="Home",padx= 5, variable=user_type, value="Home").place(x=235,y=230)
Radiobutton(root,text="Industry",padx= 20, variable=user_type, value="Industry").place(x=290,y=230)
##this creates 'Label' widget for country and uses place() method.
label_5=Label(root,text="State",width=20,font=("bold",10))
label_5.place(x=70,y=280)

#this creates list of countries available in the dropdownlist.
state_list=['TamilNadu','Kerla','Andrapradesh','Karnataka']

#the variable 'c' mentioned here holds String Value, by default ""
droplist=OptionMenu(root,state,*state_list)
droplist.config(width=15)
state.set("Select Your State")
droplist.place(x=240,y=280)
##this creates 'Label' widget for Language and uses place() method.
label_6=Label(root,text="Language",width=20,font=('bold',10))
label_6.place(x=75,y=330)
#the variable 'var1' mentioned here holds Integer Value, by default 0
#this creates Checkbutton widget and uses place() method.
def adminPage():
    root.destroy()
    import admin

def user_login():
    root.destroy()
    import user_login
def add_user():
    print("alert")
    if username.get() != "":
        all={"uname":str(username.get()),"password":str(password.get()),"user_type":str(user_type.get()),"state":str(state.get())}
        print(all)      
        dbobj.insert_data(all) 
        messagebox.showinfo("Message",all)
        root.destroy()
        import user_login
    else:    
        messagebox.showinfo("Invaild","  All The Details Required To Register")
#this creates button for submitting the details provides by the user
Button(root, text='Submit' , width=20,bg="green",fg='white',command=add_user).place(x=180,y=380)
Button(root, text='login' , width=20,bg="yellow",fg='white',command=user_login).place(x=100,y=440)
Button(root, text='admin' , width=20,bg="orange",fg='white',command=adminPage).place(x=260,y=440)
f = ("Times bold", 14)  
#this will run the mainloop.
root.mainloop()
"""
from tkinter import *
from tkinter import filedialog, messagebox
from ..product_designer import backend
from ..
import webbrowser
#194703-21871a60-f09c-4678-97b9-2db2b7322acf
# Required in order to add data files to Windows executable
import sys, os
path = getattr(sys, '_MEIPASS', os.getcwd())
os.chdir(path)


def btn_clicked():
    token = token_entry.get()
    URL = URL_entry.get()

    if not token:
        messagebox.showerror(title="Empty Fields",
                             message="Please enter Token")

    elif not URL:
        messagebox.showerror(title="Empty Fields",
                             message="Please enter URL")

    elif not output_path:
        messagebox.showerror(title="invalid path",
                             message="Enter a valid output path")

    else:
        backend.generate_code(token,URL, output_path)

def select_path(event):
    global output_path

    # window.withdraw()
    output_path = filedialog.askdirectory()
    path_entry.delete(0, END)
    path_entry.insert(0, output_path)
    # window.deiconify()


def make_label(master, x, y, h, w, *args, **kwargs):
    f = Frame(master, height=h, width=w)
    f.pack_propagate(0) # don't shrink
    f.place(x=x, y=y)

    label = Label(f, *args, **kwargs)
    label.pack(fill=BOTH, expand=1)

    return label




window = Tk()
window.title("Proxlight Designer")
window.iconbitmap("Icon.ico")
window.geometry("862x519")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 519,
    width = 862,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    374.0, 295.5,
    image=background_img)

canvas.create_text(
    220.0, 78.5,
    text = "Proxlight",
    fill = "#ffffff",
    font = ("Bite Chocolate", int(30.0)))

canvas.create_text(
    607.0, 78.5,
    text = "Enter Details Here",
    fill = "#515486",
    font = ("Roboto-Bold", int(15.0)))

canvas.create_text(
    210.0, 150,
    text = "Designer",
    fill = "#ffffff",
    font = ("Roboto-Italic", int(24.0)))

canvas.create_text(
    210.0, 280.0,
    text = "Create Some Thing Beautiful !",
    fill = "#ffffff",
    font = ("Roboto-Bold", int(13.0)))



path_entry_img = PhotoImage(file = f"img_textBox0.png")
path_entry_bg = canvas.create_image(
    638.0, 345.0,
    image = path_entry_img)

path_entry =  Entry(
    bd = 0,
    bg = "#ececec",
    highlightthickness = 0)
path_entry.place(
        x = 538.0, y = 326,
        width = 200.0,
        height = 36)


path_entry.bind("<1>", select_path)

URL_entry_img = PhotoImage(file = f"img_textBox1.png")
URL_entry_bg = canvas.create_image(
    638.0, 248.0,
    image = URL_entry_img)

URL_entry = Entry(
    bd = 0,
    bg = "#ececec",
    highlightthickness = 0)

URL_entry.place(
    x = 538.0, y = 229,
    width = 200.0,
    height = 36)

token_entry_img = PhotoImage(file = f"img_textBox2.png")
token_entry_bg = canvas.create_image(
    638.0, 153.0,
    image = path_entry_img)

token_entry = Entry(
    bd = 0,
    bg = "#ececec",
    highlightthickness = 0)

token_entry.place(
    x = 538.0, y = 134,
    width = 200.0,
    height = 36)
token_entry.focus()

canvas.create_text(
    560.5, 117.0,
    text = "Token ID",
    fill = "#9e9e9e",
    font = ("Roboto-Light", int(13.0)))

canvas.create_text(
    560.5, 210.0,
    text = "File URL",
    fill = "#9e9e9e",
    font = ("Roboto-Light", int(13.0)))

canvas.create_text(
    560.5, 310.0,
    text = "Export To",
    fill = "#9e9e9e",
    font = ("Roboto-Light", int(13.0)))

img0 = PhotoImage(file = f"img0.png")
b0 = Button(image=img0, borderwidth=0, highlightthickness=0, command=btn_clicked, relief="flat")

b0.place(
    x = 572, y = 401,
    width = 152,
    height = 51)

window.resizable(False, False)
window.mainloop()
"""