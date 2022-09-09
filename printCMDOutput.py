import subprocess

batcmd="python E:\\python\\temp.py"
result = subprocess.check_output(batcmd, shell=True)
open('E:\\python\\a.txt', 'wb').write(bytes(result))
print(result.decode('utf-8'))