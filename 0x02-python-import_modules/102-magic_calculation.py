#!/usr/bin/python3
# 102-magic_calculation.py

def magic_calculation(num1, num2):
    """Match bytecode provided by Holberton School."""
    from magic_calculation_102 import add, sub

    if num1 < num2:
        c = add(num1, num2)
        for i in range(4, 6):
            c = add(c, i)
        return (c)

    else:
        return(sub(num1, num2))
