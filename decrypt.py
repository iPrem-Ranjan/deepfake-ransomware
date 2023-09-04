import random

# Safeguard password generation
safeguard = input("enter the safeguard password: ")
if safeguard != 'start':
    quit()

encryption_level = 128//8
char_pool = ''

for i in range(0x00,0xFF):
    char_pool += chr(i)

# print(char_pool)

# key generate
key = ''
for i in range(encryption_level):
    key += random.choice(char_pool)

# encrypting a file
key_index = 0

