#!/usr/bin/python3
# 100-print_tebahpla.py
for inr in range(122, 96, -1):
    if inr % 2 != 0:
        inr = inr - 32
    print("{}".format(chr(inr)), end="")
