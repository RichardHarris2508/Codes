from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

from tkinter import *
import tkinter.messagebox as tmsg
import os
import sys
import random
import datetime
from plyer import notification
import smtplib 
from pygame import mixer
import database2.app as app
import sqlite3
#import win32.lib.win32con as win32con
#import win32gui

#the_program_to_hide = win32gui.GetForegroundWindow()
#win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)

conn = sqlite3.connect('database2\\login_dat.db')
c = conn.cursor()

try:
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls() 
    s.login("richard.harris2508@gmail.com", "starkindustries3!")
except:
    pass
    
def stop():
    try:
        mixer.music.stop()
    except:
        mixer.music.play()        

mixer.init()

mixer.music.load('database2\\zalarm.mp3')

def sendMail(mes):
    s.sendmail("richard.harris2508@gmail.com", "shoumikkesarwani@gmail.com", mes)


date = datetime.datetime.now()
time = datetime.datetime.now().strftime("Time: %H:%M:%S")

l = open('D:\\python\\database2\\login.txt', "a")

def notify(msg):
    notification.notify(title = 'Password',message = msg)

def otp_gui():

    def check():

        try:
            ot = otpVar.get()
        except:
            tmsg.showinfo("otp", "Enter an integer value")
            ot = 0


        O = o

        if ot == O:

            if uservalue == 'kesarwani.shoumik':
                tmsg.showinfo("otp", "loging you in...")
                stop()
                root.destroy()
                os.startfile('E:\\sam\\MOVIES\\tom and jerry\\Tom and Jerry\\Tom And Jerry Tales (2006 - 2008) Part 1')
                notify(f'{uservalue},successful')
                l.write("successful \n")
                try:     
                    sendMail(f'{uservalue}, failed') 
                except:
                    pass

            elif uservalue == 'richard.harris':
                tmsg.showinfo("otp", "loging you in...")
                stop()
                root.destroy()
                app.aap() 
                notify(f'{uservalue},successful')
                l.write("successful \n")
                stop()
                try:     
                    sendMail(f'{uservalue}, failed') 
                except:
                    pass

            else:
                l.write("failed \n")
                stop()
                mixer.music.play()
                notify(f'{uservalue},failed')
                try:     
                    sendMail(f'{uservalue}, failed') 
                except:
                    pass
                        
        else:
            tmsg.showinfo("otp", "wrong otp")
            l.write("failed \n")
            notify(f'{uservalue},failed') 
            try:
                sendMail(f'{uservalue}, failed')     
            except:
                pass

            stop()
            mixer.music.play()    

    fr = Frame(root).grid()

    Label(fr, text = "Enter the otp").grid(row = 3, column = 1)
    otpVar = IntVar()
    Entry(fr, textvar = otpVar).grid(row = 3, column = 2)
    Button(fr, text = "Login", command = check).grid(row = 4, column = 1)

def login(event):

    global uservalue
    global passvalue

    uservalue = username.get()
    passvalue = password.get()

    if uservalue=='richard.harris' and passvalue=='ironman':
        a = 'open'
        stop()
        tmsg.showinfo("login", "loging you in... as Richard Harris")

    elif uservalue=='kesarwani.shoumik' and passvalue=='stark':
        a = 'open'
        stop()
        tmsg.showinfo("login", "loging you in... as Shoumik Kesarwani") 

    else:
        a = 'never'
        tmsg.showinfo("login", "incorrect username or password") 
        l.write(f"{uservalue} - {date.year} / {date.month} / {date.day}  - {time} - ")
        notify(f'{uservalue},failed')
        stop()
        mixer.music.play()
        try:
            sendMail(f'{uservalue},failed')
        except:
            pass    

    if a == 'open' :
        global o

        o = random.randint(1000,9999)
        f = open('database2\\otp.txt', "a")
        f.truncate(0)
        f.write(f"otp is {o}")
        try:
            sendMail(f'otp is {o}')
        except:
            pass    

        l.write(f"{uservalue} - {date.year} / {date.month} / {date.day}  - {time} - ")

        otp_gui()

    else:
        pass

root = Tk()
root.title("Lock")
root.configure(background = "black")

frame = Frame(root, bg = "white").grid()

username = StringVar()
password = StringVar()

Label(frame, text = "Username").grid(row=1, column=1)
Entry(frame, textvar = username).grid(row=1, column=2)

Label(frame, text = "Password").grid(row=2, column=1)
Entry(frame, textvar = password, show = "*").grid(row=2, column=2)

lg = Button(frame, text = "Login")
lg.bind('<Return>', login)
lg.grid(row=3, column=1)

root.mainloop()

try:
    s.quit()
except:
    pass    