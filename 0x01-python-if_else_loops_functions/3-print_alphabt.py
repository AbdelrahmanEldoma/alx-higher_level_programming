#!/usr/bin/python3
i = 97
while i < 123:
    print("{}".format(chr(i)), end='')
    if i == 100 or i == 112:
        i = i + 1
    i = i + 1
