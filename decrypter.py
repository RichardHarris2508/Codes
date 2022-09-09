import os
import re
import sys
import json
import base64
import sqlite3
import win32crypt
from Cryptodome.Cipher import AES
import shutil
import csv

CHROME_PATH_LOCAL_STATE = (r"E:\programming\python\local state")

def get_secret_key():
    #(1) Get secretkey from chrome local state
    with open( CHROME_PATH_LOCAL_STATE, "r", encoding='utf-8') as f:
        local_state = f.read()
        local_state = json.loads(local_state)
    secret_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    #Remove suffix DPAPI
    secret_key = secret_key[5:] 
    secret_key = win32crypt.CryptUnprotectData(secret_key, None, None, None, 0)[1]
    return secret_key

def decrypt(ciphertext):
    initialisation_vector = ciphertext[3:15]
    encrypted_password = ciphertext[15:-16]
    cipher = AES.new(get_secret_key(), AES.MODE_GCM, initialisation_vector)
    decrypted_pass = cipher.decrypt(encrypted_password)
    decrypted_pass = decrypted_pass.decode()
    print(decrypted_pass)

conn = sqlite3.connect("E:\\programming\\python\\password.db")
c = conn.cursor()

c.execute("SELECT action_url, username_value, password_value, blacklisted_by_user FROM logins")

for index,login in enumerate(c.fetchall()):
    url = login[0]
    username = login[1]
    ciphertext= login[2]

    if username != '':
        print("Url: ",url)
        print("Username: ",username)
        #print("Cipher Text: ",ciphertext)
        try:
            decrypt(ciphertext)
        except:
            print('can\'t decrypt')

        print('\n\n')