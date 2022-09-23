import binascii
import sys

fileout = open("hexreadout.bin", "w")

if len(sys.argv) > 1:
    filein = open(sys.argv[1], "r")
else:
    exit

binaryData = filein.read()
filein.close()

fileout.write(binascii.hexlify(binaryData).decode())

fileout.close()