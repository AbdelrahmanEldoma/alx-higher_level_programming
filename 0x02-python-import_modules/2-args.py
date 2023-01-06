#!/usr/bin/python3
import sys


def main():
    if len(sys.argv) - 1 != 0 and len(sys.argv) - 1 != 1:
        print("{:d} arguments:".format(len(sys.argv) - 1))
        for j in range(1, len(sys.argv)):
            if j == len(sys.argv):
                print("{:d}: {:s}".format(j, sys.argv[j]), end="")
            else:
                print("{:d}: {:s}".format(j, sys.argv[j]))
    elif len(sys.argv) - 1 == 0:
        print("{:d} arguments.".format(len(sys.argv) - 1), end="")
    elif len(sys.argv) - 1 == 1:
        print("{:d} argument:".format(len(sys.argv) - 1))
        print("{:d}: {:s}".format(1, sys.argv[1]), end="")


if __name__ == "__main__":
    main()
