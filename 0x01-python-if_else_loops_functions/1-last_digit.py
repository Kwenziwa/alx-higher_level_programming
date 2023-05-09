#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)


if number >= 0:
    endmost_digit = number % 10
else:
    endmost_digit = number * -1 % 10 * -1

cust_msg = "Last digit of %d is %d and is" % (number, endmost_digit)

if endmost_digit == 0:
    print(cust_msg, "0")
elif endmost_digit > 5:
    print(cust_msg, "greater than 5")
else:
    print(cust_msg, "less than 6 and not 0")

