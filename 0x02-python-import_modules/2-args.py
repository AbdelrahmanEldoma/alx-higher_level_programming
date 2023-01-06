#!/usr/bin/python3
import sys


def main():
    for j in range(0, len(sys.argv)):
        if len(sys.argv) == 0:
            print("{:d} arguments.".format(len(sys.argv)), end="")
        elif len(sys.argv) == 1:
            print("{:d} argument:".format(len(sys.argv)))
            for i in range(0, len(sys.argv)):
                print("{:d}: {:s}".format(i + 1, sys.argv[i]), end="")
        elif j < len(sys.argv) - 1:
            print("{:d} arguments:".format(len(sys.argv)))
            for i in range(0, len(sys.argv)):
                print("{:d}: {:s}".format(i + 1, sys.argv[i]))
        else:
            print("{:d} arguments:".format(len(sys.argv)))
            for i in range(0, len(sys.argv)):
                print("{:d}: {:s}".format(i + 1, sys.argv[i]), end="")



if __name__ == "__main__":
    main()
