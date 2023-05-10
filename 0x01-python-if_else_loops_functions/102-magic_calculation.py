#!/usr/bin/python3
# 102-magic_calculation.py


def magic_calculation(num, num1, num2):
    if num < num1:
        return (num2)
    if num2 > num1:
        return (num + num1)
    return (num*num1 - num2)
