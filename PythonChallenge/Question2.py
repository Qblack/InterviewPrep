__author__ = 'Q'

letters = "abcdefghijklmnopqrstubvwxyz"

def decode(encrypted):
    decrypted = ""
    for char in encrypted:
        byte_value = ord(char)
        if ord('z') >= byte_value >= ord('a'):
            byte_value = (byte_value + 2 - ord('a')) % 26 + ord('a')

        decrypted = ''.join((decrypted, chr(byte_value)))

    return decrypted


encrypted_string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
decryption = decode(encrypted_string)
print(decryption)

url = "http://www.pythonchallenge.com/pc/def/map.html"
print(decode(url))
