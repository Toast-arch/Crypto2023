import codecs

my_string = "57656c6c20646f6e6520212054686520666c616720666f722074686973206368616c6c656e67652069732074686973206d6573736167652e"
my_string_bytes = bytes(my_string, encoding='utf-8')

binary_string = codecs.decode(my_string_bytes, "hex")
print(str(binary_string, 'utf-8'))

txt = "25 24 ee 9f 75 64 67 69 74 67 ff 64 67 69 08 67 75 64 19 69 74 67 0b 64 67 69 75 67 55 64 64 69 74"
key = "67 69 ec 5e"
get = "42 4d 00 00 f8 9a"

thi = "67 69 74 67 75 64"