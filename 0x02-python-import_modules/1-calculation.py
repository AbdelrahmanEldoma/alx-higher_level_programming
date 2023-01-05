#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def main():
    a = 10
    b = 5
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)), end="")
    print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)), end="")
    print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)), end="")
    print("{:d} / {:d} = {:d}".format(a, b, div(a, b)), end="")


if __name__ == "__main__":
    main()
