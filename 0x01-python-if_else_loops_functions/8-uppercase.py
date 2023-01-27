#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) != 32:
            print("{}".format(chr(ord(i) - 32)), end='')
        else:
            print("{}".format(chr(32)))
