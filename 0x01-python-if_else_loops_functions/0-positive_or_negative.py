#!/usr/bin/python3
import random
from enum import IntEnum

class DigitEnum(IntEnum):
    ZERO = 0
    ONE = 1

number = random.randint(-10, 10)
if number > DigitEnum.ZERO:
    print("{} is positive".format(number))
elif number == DigitEnum.ZERO:
    print("{} is zero".format(number))
else:
    print("{} is negative".format(number))
