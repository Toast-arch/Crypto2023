import sys

ciphertext = "aaa"
key = "aaa"

fileout = open("vigenereout.txt", "w")

if len(sys.argv) > 1:
    filein = open(sys.argv[1], "r")
    ciphertext = filein.read()
    filein.close()

if len(sys.argv) > 2:
    key = sys.argv[2]


def normalize(c: int) -> int:
    if c < 0:
        return c + 25
    if c > 25:
        return c - 26
    return c

def is_uppercase(c: int) -> bool:
    return c > 64 and c < 91
def is_lowercase(c: int) -> bool:
    return c > 96 and c < 123
i2 = -1
for i in range(0, len(ciphertext)):
    if not is_lowercase(ord(ciphertext[i])) and not is_uppercase(ord(ciphertext[i])):
        print(ciphertext[i], end="")
        fileout.write(ciphertext[i])
        continue
    
    if is_uppercase(ord(ciphertext[i])):
        delta = 65
    else:
        delta = 97
    
    if is_uppercase(ord(key[i2])):
        deltakey = 65
    else:
        deltakey = 97
        
    i2 += 1
    if i2 >= len(key):
        i2 = 0

    c1 = normalize(ord(ciphertext[i]) - delta)

    c2 = normalize(ord(key[i2]) - deltakey)
 
    res = normalize(c1 + c2)

    print(chr(res + delta), end="")
    fileout.write(chr(res + delta))

fileout.close()