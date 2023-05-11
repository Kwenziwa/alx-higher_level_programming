#!/usr/bin/python3
# 3-infinite_add.py
def add_arg(argv):
    num = len(argv) - 1
    if num == 0:
        print("{:d}".format(num))
        return
    else:
        i = 1
        add = 0
        while i <= num:
            add += int(argv[i])
            i += 1
        print("{:d}".format(add))


if __name__ == "__main__":
    import sys
    add_arg(sys.argv)
