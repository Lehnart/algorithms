from typing import List


def insertion_sort(array: List):
    """
    Implementation of insertion sort. the sort is not in place.
    :param array: array to be sorted
    :return: sorted array
    """

    def insert(value, sorted_sub_array: List):
        """
        Insert value at the right place so sarray is sorted
        :param value: value to insert
        :param sorted_sub_array: sorted array
        :return: sarray with value sorted
        """
        for i in range(len(sorted_sub_array)):
            if sorted_sub_array[i] >= value:
                sorted_sub_array.insert(i, value)
                return
        sorted_sub_array.append(value)

    sorted_array = []
    for i in range(len(array)):
        insert(array[i], sorted_array)
    return sorted_array


def selection_sort(array: List):
    """
    Implementation of selection sort. the sort is not in place.
    :param array: array to be sorted
    :return: sorted array
    """

    sorted_array = []
    for i in range(len(array)):
        index_min = array.index(min(array))
        sorted_array.append(array.pop(index_min))
    return sorted_array


def heap_sort(array: List):
    """
    Implementation of heap sort. the sort is in place.
    :param array: array to be sorted
    """

    def heapify(array: List, i: int):
        """
         Suppose that the array[0:i-1] is structures as a heap, adding the array[i] in ordre to keep a heap structure.
        :param array: array with a heap structure up to i-1
        :param i: element index to add to heap structure
        :return: nothing, everything is done in place
        """
        if i == 0:
            return

        curr = array[i]
        up_index = (i - 1) // 2
        up = array[up_index]
        if up < curr:
            array[up_index], array[i] = array[i], array[up_index]
            heapify(array, up_index)

    # change array structure as heap
    for i in range(1, len(array)):
        heapify(array, i)

    # swap top of heap on right of array, and restructure as a heap
    for i in range(len(array) - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        for j in range(1, i):
            heapify(array, j)

    return array
