from tkinter import *
ws = Tk()
ws.geometry('400x300')
ws.title('PythonGuides')
ws['bg']='#5d8a82'
f = ("Times bold", 14)
def unpay_user():
    ws.destroy()
    import nonpay_user
def pay_user():
    ws.destroy()
    import pay_user
Label(
    ws,
    text="Welcome to Admin Page!!! for only this Administration",
    padx=20,
    pady=20,
    bg='#5d8a82',
    font=f
).pack(expand=True, fill=BOTH)
Button(
    ws, 
    text="pay_user", 
    font=f,
    command=pay_user
    ).pack(fill=X, expand=TRUE, side=LEFT)
Button(
    ws, 
    text="unpay_user", 
    font=f,
    command=unpay_user
    ).pack(fill=X, expand=TRUE, side=LEFT)
ws.mainloop()