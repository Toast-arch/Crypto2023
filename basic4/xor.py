from operator import xor

filein = open("basic4cypher.webp", "rb")
fileout = open("basic4recovered.webp", "wb")

binaryData = filein.read()
key_byte_string = "773f763d4d7351615052324e6a5038"

key = bytes.fromhex(key_byte_string)
tmp = bytes()

for i in range(len(binaryData)):
    tmp = xor(binaryData[i], key[i % len(key)]).to_bytes(1, 'little')
    fileout.write(tmp)

fileout.close()