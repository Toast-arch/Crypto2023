import base64
import hashlib

from Crypto.Cipher import AES

plaintext = "I was lost, but now I'm found..."

bs = AES.block_size
key = hashlib.sha256("omgwtfbbq".encode()).digest()
ket = "6dba3a9589441e494d7be1eaef3a6c18c6807289f768acf8431f5f7500f56187"
iv = "????????????????".encode()

cipher = AES.new(key, AES.MODE_CBC, iv)

ciphertext = cipher.encrypt(plaintext.encode())

print(''.join(format(x, '02x') for x in ciphertext))