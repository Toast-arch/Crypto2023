
from operator import xor

filein = open("basic3cypher.bmp", "rb")
fileout = open("basic3recovered.bmp", "wb")

binaryData = filein.read()

key_byte_list = [103, 105, 116, 103, 117, 100]
key = bytes(key_byte_list)
tmp = bytes()

for i in range(len(binaryData)):
    tmp = xor(binaryData[i], key[i % len(key)]).to_bytes(1, 'little')
    fileout.write(tmp)

fileout.close()