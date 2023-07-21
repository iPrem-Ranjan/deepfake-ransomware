import PythonCrypto
import PythonCrypto.Cipher
import PythonCrypto.Random
import base64

from crypto.PublicKey import RSA

# generate RSA encryption + decryption keys / public + private keys
key = RSA.generate(2048)

private_key = key.exportKey()
with open('private.pem','wb') as f:
    f.write(private_key)

public_key = key.public_key().exportKey()
with open('public.pem','wb') as f:
    f.write(public_key)