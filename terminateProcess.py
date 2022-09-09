import wmi

ti = 0
name = 'wmpla'
f = wmi.WMI()

for process in f.Win32_Process():
    print(process.name)
    if name in process.name: 
        process.Terminate()
        ti += 1

if ti == 0:
    print("Process not found!!!")