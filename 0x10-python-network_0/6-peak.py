#!/usr/bin/python3
"""This module contains the find_peak function.
"""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers.
    """
    if not list_of_integers:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    if len(list_of_integers) == 2:
        return max(list_of_integers)

    mid = len(list_of_integers) // 2
    if list_of_integers[mid - 1] < list_of_integers[mid]\
        > list_of_integers[mid + 1]:
        return list_of_integers[mid]
    if list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    return find_peak(list_of_integers[mid + 1:])
