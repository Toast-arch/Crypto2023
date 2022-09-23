import binascii

filein = open("basic3recovered.bmp", "rb")
fileout = open("basic3outé.bmp", "w")

binaryData = filein.read()

fileout.write(str(binascii.hexlify(binaryData)))
