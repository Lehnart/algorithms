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


def binary_search(el: int, array: List) -> bool:
    """
    Use the built in function of sort and my implementation of binary search.
    :param el : searched element.
    :param array: array to be searched.
    :return: is el in array ?
    """

    array.sort()
    sub_array = array
    while True:
        if len(sub_array) == 0:
            return False
        index = len(sub_array) // 2
        cur = sub_array[index]
        if cur == el:
            return True
        elif cur > el:
            sub_array = sub_array[:index]
            continue
        else:
            sub_array = sub_array[index + 1:]
            continue


def python_binary_search(el: int, array: List) -> bool:
    """
    Use the built in function of sort and binary search.
    :param el : searched element.
    :param array: array to be searched.
    :return: is el in array ?
    """

    array.sort()
    i = bisect_left(array, el)
    return i != len(array) and array[i] == el
