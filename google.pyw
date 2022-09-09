import webbrowser
from tkinter import *
import datetime
import win32.lib.win32con as win32con
import win32gui

the_program_to_hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)

def classroom():
    root1 = Tk()

    lab = Label(root1)
    lab.pack()

    def clock():
        time = datetime.datetime.now().strftime("Time: %H:%M:%S")
        lab.config(text = time)
        lab.after(1000, clock) 

    def a():
        chrome_path="C:\\Users\\hp\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe"
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

    a()
        
    frame = Frame(root1, borderwidth = "10", bg = "grey", relief = SUNKEN)
    frame.pack(side = "left", anchor = "nw")

    frame1 = Frame(root1, borderwidth = "10", bg = "grey", relief = SUNKEN)
    frame1.pack(side = "bottom", anchor = "ne")

    Label(clock()).pack()

    def geo():
        webbrowser.get('chrome').open_new_tab("https://classroom.google.com/u/1/c/MTI1NzQ4MjU4MTE0")

    def maths():
        webbrowser.get('chrome').open_new_tab("https://classroom.google.com/u/1/c/NzEyNTE0NzE4NTFa")
    
    def physics():
        webbrowser.get('chrome').open_new_tab("https://classroom.google.com/u/1/c/MTQxMTIzODY0MDE0")

    def chemistry():
        webbrowser.get('chrome').open_new_tab("https://classroom.google.com/u/1/c/MTIyMDE1MjY2MjYw")
    
    def computer():
        webbrowser.get('chrome').open_new_tab("https://classroom.google.com/u/1/c/OTU2NTUwODE5ODda")

    def bio():
        webbrowser.get('chrome').open_new_tab("https://classroom.google.com/u/1/c/MTAwODEyODc2NzAz")
        
    def history():
        webbrowser.get('chrome').open_new_tab("https://classroom.google.com/u/1/c/MTEwMzYxNzI1MjIz")
        
    def english():
        webbrowser.get('chrome').open_new_tab("https://classroom.google.com/u/1/c/MTAxMDIwMzA5MDMw")
        
    def hindi():
        webbrowser.get('chrome').open_new_tab("https://classroom.google.com/u/1/c/NTYxMjU2MjQyNDBa")
    
    def exit():
        root1.destroy()    

    Button(frame, text = "Maths", command = maths).grid(row = 1, column = 1)
    Button(frame, text = "Physics", command = physics).grid(row = 1, column = 2)
    Button(frame, text = "Chemistry", command = chemistry).grid(row = 1, column = 3)
    Button(frame, text = "Computer", command = computer).grid(row = 1, column = 4)
    Button(frame, text = "Biology", command = bio).grid(row = 2, column = 1)
    Button(frame, text = "Geography", command = geo).grid(row = 2, column = 2)
    Button(frame, text = "History", command = history).grid(row = 2, column = 3)
    Button(frame, text = "English", command = english).grid(row = 2, column = 4)
    Button(frame, text = "Hindi", command = hindi).grid(row = 3, column = 1)
    Button(frame1, text = "EXIT", command = exit).grid(row = 4, column = 2)

    root1.mainloop()

chrome_path="C:\\Users\\hp\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe"

webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

def exit():
    root.destroy()

def ig():
    webbrowser.get('chrome').open_new_tab("https://www.instagram.com/")

def wa():   
    webbrowser.get('chrome').open_new_tab("https://web.whatsapp.com/") 

def yt():
    webbrowser.get('chrome').open_new_tab("https://www.youtube.com/") 

def mail():
    webbrowser.get('chrome').open_new_tab("https://mail.google.com/mail/?tab=rm&authuser=0&ogbl")

def gcr():
    classroom()

root = Tk()
root.title("shortcut")
root.wm_iconbitmap("icon.ico")

frame = Frame(root, borderwidth = "10", bg = "grey", relief = SUNKEN)
frame.pack(side = "left", anchor = "nw")

lab = Label(root)
lab.pack()

def clock1():
    time = datetime.datetime.now().strftime("Time: %H:%M:%S")
    lab.config(text = time)
    lab.after(1000, clock1)

Label(clock1()).pack(side = "top")    

Button(frame, text = "instagram", command = ig).grid(row = 1, column = 1)
Button(frame, text = "whatsapp", command = wa).grid(row = 2, column = 1)
Button(frame, text = "youtube", command = yt).grid(row = 3, column = 1)
Button(frame, text = "gmail", command = mail).grid(row = 4, column = 1)
Button(frame, text = "GCR", command = gcr).grid(row = 5, column = 1)
Button(frame, text = "exit", command = exit).grid(row = 7, column = 2)

root.mainloop()