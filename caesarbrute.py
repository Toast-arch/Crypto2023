import sys

ciphertext = "Pwv dv idtv, bmru S mdj lscru wz vmr emdtr duj vwqurj vx xvmrq zdqvt, Lxiiwh bdt fxwuj."

if len(sys.argv) > 1:
    filein = open(sys.argv[1], "r")
    ciphertext = filein.read()
    filein.close()

for i in range(0, 25):
    print(str(i) + ". ", end="")
    for el in ciphertext:
        if ord(el) - 97 < 0 or ord(el) - 97 > 25:
            print(el, end="")
            continue
        
        c = ord(el) - 97 + i
        if c > 25:
            c -= 26
        
        print(chr(c + 97), end="")
    print("")