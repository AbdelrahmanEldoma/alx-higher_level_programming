#!/usr/bin/python3
import sys

for i in range(0, len(sys.argv) - 1):
    print("{:d} arguments:".format(len(sys.argv)))
    print("{:d}: {:s}".format(i + 1, sys.argv[i]))
