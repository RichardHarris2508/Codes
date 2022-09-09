import pywhatkit as kit

import datetime

current_time=datetime.datetime.now()

hour=current_time.hour
minute=current_time.minute

kit.sendwhatmsg("+91 9616172378","namaste", hour, minute+1)
kit.send_file("+91 9616172378","yt.py",hour, minute+1)