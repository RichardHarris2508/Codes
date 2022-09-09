import smtplib 
  
# list of email_id to send the mail 
li = ["manishashoumik@gmail.com", ""] 
  
for dest in li: 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls() 
    s.login("shoumikkesarwani@gmail.com", "starkindustries3!") 
    message = "namaste"
    s.sendmail("shoumikkesarwani@gmail.com", dest, message) 
    s.quit() 