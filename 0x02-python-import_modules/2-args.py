#!/usr/bin/python3
import sys

for i in range(1, len(sys.argv)):
    print("{:d} arguments:".format(len(sys.argv)))
    print("{:d}: {:s}".format(i, sys.argv[i]))
