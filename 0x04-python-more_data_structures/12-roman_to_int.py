#!/usr/bin/python3
# 12-roman_to_int.py
def roman_to_int(r_string: str):
    if r_string is None or type(r_string) != str:
        return 0
    my_data = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    nums = [my_data[x] for x in r_string] + [0]
    rep = 0

    for i in range(len(nums) - 1):
        if nums[i] >= nums[i+1]:
            rep += nums[i]
        else:
            rep -= nums[i]

    return rep
