#!/usr/bin/python3
def multiple_returns(asentence):
    length = len(asentence)
    first_char = asentence[0] if length > 0 else "None"
    tup = length, first_char
    return(tup)
