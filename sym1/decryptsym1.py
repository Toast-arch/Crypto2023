import base64
import codecs
import hashlib
from operator import xor
from pydoc import plain
from tabnanny import check

from Crypto.Cipher import AES

ogplaintext = "I was lost, but now I'm found..."
ogplaintext_block1 = "I was lost, but "
ogplaintext_block2 = "now I'm found..."

#ogplainttexthex = "4920776173206c6f73742c20627574206e6f772049276d20666f756e642e2e2e"
#ogciphertexthex = "00f374a82db50b2300000b88f1d976ddc1cf6db4524aac04e222853969367e0d"
#key_str_hex = "6dba3a9589441e494d7be1eaef3a6c18c6807289f768acf8431f5f7500f56187"

#ciphertexthextry = "c1cf6db4524aac04e222853969367e0d"

#cda67d2190ce89ce8f350113b9cfef05 ccaf25ed55f288ed1ae843a781cbbe77
#cda67d2190ce89ce8f350113b9cfef05 c2c052cd1cd5e5cd7c8736c9e5e59059

bs = AES.block_size
key = hashlib.sha256("omgwtfbbq".encode()).digest()
iv = "0000000000000000".encode()

#possibleiv = "c2c052cd1cd5e5cd7c8736c9e5e59059"

#hugo = AES.new(key, AES.MODE_CBC, iv)
#ciphertext = hugo.encrypt(ogplaintext.encode())

#block1 = "00f374a82db50b23"
#block2 = "00000b88f1d976dd"
#block3 = "c1cf6db4524aac04"
#block4 = "e222853969367e0d"

block1 = "00f374a82db50b2300000b88f1d976dd"
block2 = "c1cf6db4524aac04e222853969367e0d"


full = block1 + block2

ogtexthex = "4920776173206c6f73742c2062757420"
#got this by encrypting with iv = 00000000
blockt = "2687a530560918beba65017710fd5f02"

#hugot = AES.new(key, AES.MODE_ECB)
#output = hugot.decrypt(bytes.fromhex(blockt))
#hexoutput = ''.join(format(x, '02x') for x in output)
#possibleiv = bytes([_a ^ _b for _a, _b in zip(output, bytes.fromhex(ogtexthex))]).decode()

def check_result(plaintext: str, ivt: str, expected: str):
    keyt = hashlib.sha256("omgwtfbbq".encode()).digest()
    tmpaes = AES.new(keyt, AES.MODE_CBC, bytes.fromhex(ivt))
    out = tmpaes.encrypt(plaintext.encode())
    return ''.join(format(x, '02x') for x in out) == expected

#print(check_result(ogplaintext_block1, possibleiv, blockt))

#print(''.join(format(x, '02x') for x in ciphertext))
#print(ogciphertexthex)

hexcharlist = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

def replace_missing_values(ogstring , i1 = 0, i2= 0, i3= 0, i4= 0, i5= 0):
    ogstringlist = list(ogstring)
    ogstringlist[0] = hexcharlist[i1]
    ogstringlist[1] = hexcharlist[i2]
    ogstringlist[16] = hexcharlist[i3]
    ogstringlist[17] = hexcharlist[i4]
    ogstringlist[18] = hexcharlist[i5]
    return ''.join(ogstringlist)

#print("I was lost, but ")
#print("4920776173206c6f73742c2062757420")
#print(''.join(format(x, '02x') for x in ogplaintext_block1.encode()))


for i1 in range(0, 16):
    for i2 in range(0, 16):
        for i3 in range(0, 16):
            for i4 in range(0, 16):
                for i5 in range(0, 16):
                    block1 = replace_missing_values(block1, i1, i2, i3, i4, i5)

                    #print("TRYING {:02d} {:02d} {:02d} {:02d} {:02d} ::: {}".format(i1, i2, i3, i4, i5, block1))

                    key = hashlib.sha256("omgwtfbbq".encode()).digest()
                    hugo2 = AES.new(key, AES.MODE_ECB)
                    output = hugo2.decrypt(bytes.fromhex(block1))
                    hexoutput = ''.join(format(x, '02x') for x in output)
                    #print("DECRYPT ECB           ::: {}".format(hexoutput))
                    
                    #print(xor_strings(hexoutput, ogtexthex))
                    #xorstr = xor_strings(hexoutput, ogtexthex)
                    #print("GONNA DO XOR")
                    #print(hexoutput)
                    #print(ogtexthex)
                    possibleivhexstr = hex(int(block1, 16) ^ int(hexoutput, 16))[2:]
                    while len(possibleivhexstr) < 32:
                        possibleivhexstr = "0" + possibleivhexstr
                    #print(possibleivhexstr)

                    #print("XOR RESULT            ::: " + possibleivhexstr)
                    #print(codecs.decode(bytes(possibleivhexstr, encoding='utf-8'), "hex"))
                    #print(''.join(format(x, '02x') for x in xorstr.encode()))
            
                    #print(bytes([_a ^ _b for _a, _b in zip(output, bytes.fromhex(ogtexthex))]).decode())


                    if check_result(ogplaintext_block1, possibleivhexstr, block1):
                        print(possibleivhexstr)
                        exit()
                    #print("DONE")

