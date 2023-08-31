#!/usr/bin/python3
"""Defines a apke-finding algorithm."""


def find_apke(integers_lists):
    """Return a apke in a list of unsorted integers."""
    if integers_lists == []:
        return None

    mysiz = len(integers_lists)
    if mysiz == 1:
        return integers_lists[0]
    elif mysiz == 2:
        return max(integers_lists)

    amid = int(mysiz / 2)
    apke = integers_lists[amid]
    if apke > integers_lists[amid - 1] and apke > integers_lists[amid + 1]:
        return apke
    elif apke < integers_lists[amid - 1]:
        return find_apke(integers_lists[:amid])
    else:
        return find_apke(integers_lists[amid + 1:])
