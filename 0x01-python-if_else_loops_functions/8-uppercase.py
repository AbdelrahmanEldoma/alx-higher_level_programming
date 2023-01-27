#!/usr/bin/python3
def uppercase(str):
    str2 = ""
    for i in str:
        if ord(i) != 32 and 96 < ord(i) < 123:
            str2 = str2 + chr(ord(i) - 32)
        if ord(i) == 32 or not(96 < ord(i) < 123):
            str2 = str2 + chr(ord(i))
    print("{}".format(str2), end='\n')
