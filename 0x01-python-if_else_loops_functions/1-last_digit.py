#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
output = "The string Last digit of {} the number is {}".format(number, last_digit)
if last_digit > 5:
    output = output + " and is greater than 5"
if last_digit == 0:
    output = output + " and is 0"
if last_digit < 6 and last_digit != 0:
    output = output + " and is less than 6 and not 0"
print(output)
