#!/usr/bin/python3
import sys


def main():
    if len(sys.argv) == 0:
        print("{:d} arguments.".format(len(sys.argv)), end="")
    elif len(sys.argv) == 1:
        print("{:d} argument:".format(len(sys.argv)))
        print("{:d}: {:s}".format(1, sys.argv[0]), end="")
    else:
        for j in range(1, len(sys.argv)):
            if j == len(sys.argv):
                print("{:d} arguments:".format(len(sys.argv)))
                print("{:d}: {:s}".format(j, sys.argv[j]), end="")
            else:
                print("{:d} arguments:".format(len(sys.argv)))
                print("{:d}: {:s}".format(j, sys.argv[j]))


if __name__ == "__main__":
    main()
