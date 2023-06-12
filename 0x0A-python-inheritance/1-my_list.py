#!/usr/bin/python3

"""
A class MyList that inherits from list
"""

MyList = __import__('1-my_list').MyList

alist = MyList()
alist.append(1)
alist.append(4)
alist.append(2)
alist.append(3)
alist.append(5)

print(alist)
alist.print_sorted()
print(alist)
