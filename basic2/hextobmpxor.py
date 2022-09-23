
from operator import xor

filein = open("basic3out.bmp", "rb")
fileout = open("basic3recovered.bmp", "wb")

binaryData = filein.read()
lit = [103, 105, 116, 103, 117, 100]
key = bytes(lit)
print(''.join(format(x, '02x') for x in key))
res = bytes(lit)

for i in range(len(binaryData)):
    res = xor(binaryData[i], key[i % len(key)]).to_bytes(1, 'little')
    fileout.write(res)

fileout.close()