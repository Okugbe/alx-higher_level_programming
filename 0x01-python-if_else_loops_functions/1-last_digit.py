#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
output = "The string Last digit of {} the number is {}".format(number, last_digit)
if last_digit > 5:
    print("Last digit of {:d} is {:d} and is greater than 5"
          .format(number, lastdigit))
if last_digit == 0:
    print("Last digit of {:d} is 0 and is 0".format(number))
if last_digit < 6 and last_digit != 0:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0"
          .format(number, lastdigit))
