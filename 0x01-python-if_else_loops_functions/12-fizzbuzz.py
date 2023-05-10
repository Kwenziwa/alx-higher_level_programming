#!/usr/bin/python3
# 12-fizzbuzz.py


def fizzbuzz():
    for anums in range(1, 101):
        if anums % 3 == 0 and anums % 5 == 0:
            print("FizzBuzz ", end="")
        elif anums % 3 == 0:
            print("Fizz ", end="")
        elif anums % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(anums), end="")
