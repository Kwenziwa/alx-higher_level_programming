#!/usr/bin/python3
#  Prints the number of and the list of its arguments
if __name__ == "__main__":
    import sys

    arg = sys.argv
    count_size = len(arg) - 1

    if count_size > 1:
        print("{} arguments:".format(count_size))
        for i in range(1, count_size + 1):
            print("{}: {}".format(i, arg[i]))

    elif count_size == 0:
        print("{} arguments.".format(count_size))

    else:
        print("{} argument:".format(count_size))
        print("{}: {}".format(count_size, arg[1]))
