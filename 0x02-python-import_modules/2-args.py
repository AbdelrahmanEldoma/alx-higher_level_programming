#!/usr/bin/python3
import sys


def main():
    print("{:d} arguments:".format(len(sys.argv)))
    for i in range(1, len(sys.argv)):
        print("{:d}: {:s}".format(i, sys.argv[i]))


if __name__ == "__main__":
    main()
