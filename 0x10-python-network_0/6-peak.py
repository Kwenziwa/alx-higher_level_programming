#!/usr/bin/python3
"""Defines a apke-finding algorithm."""


def find_apke(list_of_integers):
    """Return a apke in a list of unsorted integers."""
    if list_of_integers == []:
        return None

    mysiz = len(list_of_integers)
    if mysiz == 1:
        return list_of_integers[0]
    elif mysiz == 2:
        return max(list_of_integers)

    amid = int(mysiz / 2)
    apke = list_of_integers[amid]
    if apke > list_of_integers[amid - 1] and apke > list_of_integers[amid + 1]:
        return apke
    elif apke < list_of_integers[amid - 1]:
        return find_apke(list_of_integers[:amid])
    else:
        return find_apke(list_of_integers[amid + 1:])
