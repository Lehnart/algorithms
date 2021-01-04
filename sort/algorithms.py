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

    def heapify(heap_array: List, heap_size: int, root_index: int):
        """
         Suppose that the array[0:i-1] is structures as a heap, adding the array[i] in ordre to keep a heap structure.
        :param heap_array: array with a heap structure up to i-1
        :param heap_size : size of heap, smaller or equal to array size
        :param root_index: element index to add to heap structure
        :return: nothing, everything is done in place
        """

        largest = root_index
        left = 2 * root_index + 1
        right = 2 * root_index + 2

        if left < heap_size and heap_array[left] > heap_array[largest]:
            largest = left
        if right < heap_size and heap_array[right] > heap_array[largest]:
            largest = right

        if largest != root_index:
            heap_array[root_index], heap_array[largest] = heap_array[largest], heap_array[root_index]
            heapify(heap_array, heap_size, largest)

    # change array structure as heap
    n = len(array)
    for i in range((n // 2) - 1, -1, -1):
        heapify(array, n, i)

    # swap top of heap on right of array, and restructure as a heap
    for i in range(len(array) - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)

    return array


def quick_sort(array: List):
    """
    Implementation of quick sort. the sort is in place.
    :param array: array to be sorted
    """

    if len(array) <= 1:
        return array
    pivot_index = 0
    pivot = array[pivot_index]
    pivoted_array = [pivot]
    for el in array[1:]:
        if el > pivot:
            pivoted_array.append(el)
        else:
            pivoted_array.insert(0, el)
            pivot_index += 1

    left_array = pivoted_array[:pivot_index]
    right_array = pivoted_array[pivot_index + 1:]
    sorted_left_array = quick_sort(left_array)
    sorted_right_array = quick_sort(right_array)

    return sorted_left_array + [pivot] + sorted_right_array


def python_sort(array: List):
    """
    Use the built in sort function of python
    :param array: array to be sorted
    """
    array.sort()
    return array


def merge_sort(array: List):
    """
    Implementation of merge sort. the sort is not in place.
    :param array: array to be sorted
    """

    if len(array) <= 1:
        return array

    if len(array) == 2:
        if array[0] <= array[1]:
            return array
        array.reverse()
        return array

    i = len(array) // 2
    array1, array2 = array[:i].copy(), array[i:].copy()
    array1, array2 = merge_sort(array1), merge_sort(array2)

    i1, i2 = 0, 0
    cur1, cur2 = array1[i1], array2[i2]
    sorted_array = []
    while i1 < len(array1) or i2 < len(array2):
        if i1 < len(array1) and i2 < len(array2):
            if cur1 <= cur2:
                sorted_array.append(cur1)
                i1 += 1
                cur1 = None if i1 >= len(array1) else array1[i1]

            elif cur2 <= cur1:
                sorted_array.append(cur2)
                i2 += 1
                cur2 = None if i2 >= len(array2) else array2[i2]

        else:
            if i2 == len(array2):
                sorted_array.append(cur1)
                i1 += 1
                cur1 = None if i1 >= len(array1) else array1[i1]

            elif i1 == len(array1):
                sorted_array.append(cur2)
                i2 += 1
                cur2 = None if i2 >= len(array2) else array2[i2]

    return sorted_array
