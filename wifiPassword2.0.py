from subprocess import check_output
from os import system

a = check_output('netsh wlan show profiles', shell=True).decode('utf-8')

import re

a = re.split('All User Profile     :' ,a)

for i in range(1,len(a)):
    c = a[i]

    print(c)
    e = check_output('netsh wlan show profiles \"'+c[1:len(c)-4]+'\" key = clear', shell = True)
    print(e.decode('utf-8'))
    open('a.txt', 'wb').write(e)

c = a[len(a)-1]
c = c.replace('\n','')
print(c)
e = check_output('netsh wlan show profiles \"'+c[1:len(c)]+'\" key = clear', shell = True)
open('a.txt', 'wb').write(e)