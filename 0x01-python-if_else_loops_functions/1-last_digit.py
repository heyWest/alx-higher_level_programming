#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    print(f"Last digit of {number:d} is {number % 10}", end='')
    if (number % 10) > 5:
        print(" and is greater than 5")
    elif (number % 20) == 0:
        print(" and is 0")
    else:
        print(" and is less than 6 and not 0")
else:
    print(f"Last digit of {number:d} is {number % -10}", end='')
    print(" and is less than 6 and not 0")
