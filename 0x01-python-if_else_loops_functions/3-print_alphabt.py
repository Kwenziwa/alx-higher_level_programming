#!/usr/bin/python3
for all_letters in range(97, 123):
    if (all_letters != 101 and all_letters != 113):
        print("{:c}".format(all_letters), end='')
