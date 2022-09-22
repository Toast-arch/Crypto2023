import sys

referkey = "abcdefghijklmnopqrstuvwxyz"
alphakey = "xwvacfgmldkghdobreisntuoyp"

fileout = open("monosubout.txt", "w")

if len(sys.argv) > 1:
    filein = open(sys.argv[1], "r")
    ciphertext = filein.read()
    filein.close()
else:
    sys.exit()

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

for i in range(0, len(ciphertext)):
    if not is_lowercase(ord(ciphertext[i])) and not is_uppercase(ord(ciphertext[i])):
        print(ciphertext[i], end="")
        fileout.write(ciphertext[i])
        continue
    
    if is_uppercase(ord(ciphertext[i])):
        delta = 65
    else:
        delta = 97

    c1 = normalize(ord(ciphertext[i]) - delta)
 
    res = alphakey[c1]

    if  alphakey[c1] != referkey[c1] or alphakey[c1] == "k" or alphakey[c1] == "y" or alphakey[c1] == "f":
        res = res.upper()
    elif len(sys.argv) == 2:
        res = "_"

    print(res, end="")
    fileout.write(res)

fileout.close()