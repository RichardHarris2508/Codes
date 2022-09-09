a = open('file.txt', 'rb').read()
b = str((a).decode())
c = b.split('\n')

def nameCount(n):

    f=0
    count=0

    for i in c:
        d = i.split('-')
        e = d[len(d)-1]
        #print(e)    

        if ':' in e:
            f = e.index(":")

        name = e[1:f]

        if n in name:
            count += 1

    print(f'{n}\t-\t{count}')

arr = ['Rod', 'Shoumik']

for j in arr:
    nameCount(j)