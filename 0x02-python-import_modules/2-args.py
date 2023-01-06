#!/usr/bin/python3
import sys


def main():
    if len(sys.argv) == 0:
        print("{:d} arguments.".format(len(sys.argv)))
    else:
        print("{:d} arguments:".format(len(sys.argv)))
        for i in range(1, len(sys.argv)):
            print("{:d}: {:s}".format(i, sys.argv[i]))


if __name__ == "__main__":
    main()
