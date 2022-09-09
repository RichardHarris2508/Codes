import sqlite3

conn = sqlite3.connect('E:\\programming\\python\\password.db')
c = conn.cursor()

c.execute("SELECT * FROM sqlite_master ")

for i, login in enumerate(c.fetchall()):
    print(login)