from typing import List


def insertion_sort(array: List):

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
