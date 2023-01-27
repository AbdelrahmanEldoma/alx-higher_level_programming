#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) != 32 and 96 < ord(i) < 123:
            print("{}".format(chr(ord(i) - 32)), end='')
        if ord(i) == 32 or not(96 < ord(i) < 123):
            print("{}".format(chr(ord(i))), end='')
