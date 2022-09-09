from ipregistry import IpregistryClient
import smtplib 

def send(message):
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls() 
    s.login("richard.harris2508", "starkindustries3!") 
    s.sendmail("richard.harris2508", 'shoumikkesarwani@gmail.com', message) 
    s.quit() 

def find(ip):
    a = (str(IpregistryClient("iknz4eviwyw5fp").lookup(ip)))
    print(a)
    #send(a)

#2401:4900:44dc:166b:be8d:20ee:4843:99df
find('')