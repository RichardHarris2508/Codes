def pr():
    username = userval.get()
    password = passval.get()
    root.destroy()
    
    val = f'Username: {username}\nPassword: {password}'
    return val

from tkinter import *

root = Tk()

userval = StringVar()
passval = StringVar()

Label(root, text = "Username:").grid(row=1, column=1)
Label(root, text = "Password:").grid(row=2, column=1)

Entry(root, textvariable = userval).grid(row=1, column=2)
Entry(root, show = '*', textvariable = passval).grid(row=2, column=2)

Button(root, text = "Login", command = pr).grid(row=3, column = 1)

root.mainloop()