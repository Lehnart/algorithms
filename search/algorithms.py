from bisect import bisect_left
from typing import List


def sequential_search(el: int, array: List) -> bool:
    """
    Implementation of sequential search.
    It just runs through all elements until it finds el.
    :param el : searched element.
    :param array: array to be searched.
    :return: is el in array ?
    """

    for i in range(len(array)):
        if el == array[i]:
            return True
    return False


def python_search(el: int, array: List) -> bool:
    """
    Use the built in function of search with in keyword.
    :param el : searched element.
    :param array: array to be searched.
    :return: is el in array ?
    """

    return el in array


def python_sorted_search(el: int, array: List) -> bool:
    """
    Use the built in function of sort and binary search.
    :param el : searched element.
    :param array: array to be searched.
    :return: is el in array ?
    """

    array.sort()
    i = bisect_left(array, el)
    return i != len(array) and array[i] == el
