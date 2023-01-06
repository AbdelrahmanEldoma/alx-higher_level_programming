#!/usr/bin/python3
import sys


def main():
    if len(sys.argv) == 0:
        print("{} arguments.".format(len(sys.argv)))
    elif len(sys.argv) == 1:
        print("{} argument:".format(len(sys.argv)))
        for i in range(0, len(sys.argv)):
            print("{}: {}".format(i + 1, sys.argv[i]))
    else:
        print("{} arguments:".format(len(sys.argv)))
        for i in range(0, len(sys.argv)):
            print("{}: {}".format(i + 1, sys.argv[i]))


if __name__ == "__main__":
    main()
