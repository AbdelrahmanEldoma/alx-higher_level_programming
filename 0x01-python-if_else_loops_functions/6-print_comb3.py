#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if "{}{}".format(i, j) != "{}{}".format(j, i) and i < j and "{}{}".format(i, j) != "89":
            print("{}{},".format(i, j), end=" ")
        elif "{}{}".format(i, j) != "{}{}".format(j, i) and i < j and "{}{}".format(i, j) == "89":
            print("{}{}".format(i, j), end="")