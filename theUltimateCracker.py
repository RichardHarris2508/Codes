'''import hashlib

print(hashlib.md5(input("Enter password:\n").encode('utf-8')).hexdigest())'''

def sound():
	import winsound
	from time import sleep

	for i in range(0,4):
	    winsound.Beep(9000,750)
	    sleep(0.1)

a = 'abcdefghijklmnopqrstuvwxyz1234567890-.?()!@#$%^&*_-'
b = 'abcdefghijklmnopqrstuvwxyz1234567890`~!@#$%^&*()-_+=[]\\}{|;\'\":<>,.?/*'

ch = 'aaaaaaa'

import time

t1 = time.time()
print(t1)

for i in range(0, len(a)):	
	ch = '' + a[i]
	for i in range(0, len(a)):
		ch = ch[0:0] + a[i]
		for i in range(0, len(a)):
			ch = ch[0:1] + a[i]
			for i in range(0, len(a)):
				ch = ch[0:2] + a[i]
				for i in range(0, len(a)):
					ch = ch[0:3] + a[i]
					for i in range(0, len(a)):
						ch = ch[0:4] + a[i]
						for i in range(0, len(a)):
							ch = ch[0:5] + a[i]
							for i in range(0, len(a)):
								ch = ch[0:6] + a[i]
								#print(ch)
								if ch == 'baaaaaa':
									print(time.time())
									print(time.time()-t1)
									print(ch)
									sound()
									quit()