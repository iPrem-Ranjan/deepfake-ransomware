import random

# safeguard password
safeguard_password = input("Enter your safeguard password: ")
if safeguard_password != 'start':
    quit()

# message input
msg = input('Enter any message :')
# print(f'Original message: {msg}')

encryption_level = 128//8
char_pool = ''

for i in range(0x00, 0x255):
    char_pool += chr(i)

# key generate
key = ''
for i in range(encryption_level):
    key += random.choice(char_pool)

# encrypt file
key_index = 0
max_key_index = encryption_level - 1
encrypted_msg = ''
for char in msg:
    encrypted_char = ord(char) ^ ord(key[key_index])
    encrypted_msg += chr(encrypted_char)
    if key_index >= max_key_index:
        key_index = 0
    else:
        key_index += 1
print(f'Encrypted message: {encrypted_msg}')


# decrypt file
key_index = 0
decrypted_msg = ''
for char in encrypted_msg:
    decrypted_char = ord(char) ^ ord(key[key_index])
    decrypted_msg += chr(decrypted_char)
    if key_index >= max_key_index:
        key_index = 0
    else:
        key_index += 1
print(f'Decrypted message: {decrypted_msg}')
