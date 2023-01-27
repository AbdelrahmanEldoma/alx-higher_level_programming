#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) != 32:
            print(chr(ord(i) - 32), end='')
        else:
            print(chr(32))
