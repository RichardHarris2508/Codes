import hashlib
import p

username = input("username....\t")
password = input("password....\t")

def login(password):

    if str(hashlib.md5(password.encode()).hexdigest()) == '0b1c6bc310f61b47b44e9d582cc73825':
        p.pr()
    else:
        exit()

login(password)