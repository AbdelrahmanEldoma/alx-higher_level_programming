#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number == 0:
    print(f"Last digit of {number:d} is {number % 10:d} and is 0")
if number % 10 > 5 and number > 0:
    print(f"Last digit of {number:d} is {number % 10:d} and is greater than 5")
if number % 10 < 6 and number % 10 != 0 and number > 0:
    print(f"Last digit of {number:d} is {number % 10:d} and is less than 6 and not 0")
if number % 10 == 0 and number > 0:
    print(f"Last digit of {number:d} is {number % 10:d} and is 0")
if number % 10 > 5 and number < 0:
    print(f"Last digit of {number:d} is {(number * -1) % 10 * -1:d} "
          f"and is greater than 5")
if number % 10 < 6 and number != 0 and number < 0:
    print(f"Last digit of {number:d} is {(number * -1) % 10 * -1:d} "
          f"and is less than 6 and not 0")
if number % 10 == 0 and number < 0:
    print(f"Last digit of {number:d} is "
          f"{(number * -1) % 10 * -1:d} and is 0")
