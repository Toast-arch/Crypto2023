import binascii

filein = open("basic3cyper.bmp", "rb")
fileout = open("hexreadout.bin", "w")

binaryData = filein.read()

fileout.write(str(binascii.hexlify(binaryData)))
