from os import system

def screen_record(name, time):
    system(f"E:\\programming\\platform-tools\\adb.exe shell screenrecord /storage/emulated/0/{name} --time-limit {time}")
    download(f"/storage/emulated/0/{name}",f"{name}")
    remove(f"/storage/emulated/0/{name}")

def tap(tap_x, tap_y):
    system("E:\\programming\\platform-tools\\adb.exe shell input tap {} {}".format(tap_x, tap_y))

def take_screenshot(final):
    system(f"E:\\programming\\platform-tools\\adb.exe exec-out screencap -p > {final}.png")

def swipe(start_x, start_y, end_x, end_y, duration_ms):
    system("E:\\programming\\platform-tools\\adb.exe shell input swipe {} {} {} {} {}".format(start_x, start_y, end_x, end_y, duration_ms))

def download(path, output_path):
    system(f"E:\\programming\\platform-tools\\adb.exe pull {path} {output_path}")

def remove(path):
    system(f"E:\\programming\\platform-tools\\adb.exe shell rm {path}")

def open_url(url):
    system(f'E:\\programming\\platform-tools\\adb.exe shell am start -a android.intent.action.VIEW -d {url}')

def switch_phone_on_off():
    system("E:\\programming\\platform-tools\\adb.exe shell input keyevent 26")

def press(key):
    system(f'E:\\programming\\platform-tools\\adb.exe shell input keyevent KEYCODE_{key}')

def call(number):
    system(f"E:\\programming\\platform-tools\\adb.exe shell am start -a android.intent.action.CALL -d tel:{number}")

def unlock(passcode):
    switch_phone_on_off()
    swipe(200, 2000, 200, 1500, 100)
    for i in (passcode):
        press(i)

while True:
    try:
        exec(input("Enter command:\t"))
        print("Executed successfully...")

    except:
        print("Coudn't execute!!!")