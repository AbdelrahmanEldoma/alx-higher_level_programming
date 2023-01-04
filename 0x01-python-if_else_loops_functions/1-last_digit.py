#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(f"{number:d}")
if number > 0:
    number = number % 10
if number < 0:
    number = (number * -1) % 10
print(f"{number:d}")
