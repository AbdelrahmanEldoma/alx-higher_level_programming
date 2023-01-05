#!/usr/bin/python3
import calculator_1


def main():
    a = 10
    b = 5
    print("{:d} + {:d} = {:d}".format(a, b, calculator_1.add(a, b)), end="")
    print("{:d} - {:d} = {:d}".format(a, b, calculator_1.sub(a, b)), end="")
    print("{:d} * {:d} = {:d}".format(a, b, calculator_1.mul(a, b)), end="")
    print("{:d} / {:d} = {:d}".format(a, b, calculator_1.div(a, b)), end="")


if __name__ == "__main__":
    main()
