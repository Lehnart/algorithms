import collections
import random
import unittest

import algorithms

MIN_INT = -1000
MAX_INT = 1000
MIN_LENGTH = 1
MAX_LENGTH = 250


class SortTest(unittest.TestCase):

    def setUp(self):
        self.entries = [[random.randint(MIN_INT, MAX_INT) for _ in range(n)] for n in range(MIN_LENGTH, MAX_LENGTH + 1)]

    def is_sorted(self, array):
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                return False
        return True

    def test_insertion_sort(self):
        sort_function = algorithms.insertion_sort
        self._test_sort(sort_function)

    def test_selection_sort(self):
        sort_function = algorithms.selection_sort
        self._test_sort(sort_function)

    def _test_sort(self, sort_function):
        for i in range(len(self.entries)):
            with self.subTest(i=i):
                array = self.entries[i]
                original_array = list(array)
                sorted_array = sort_function(array)

                self.assertEqual(len(original_array), len(sorted_array))
                self.assertTrue(self.is_sorted(sorted_array))

                original_array_dict = collections.Counter(original_array)
                sorted_array_dict = collections.Counter(sorted_array)
                self.assertDictEqual(original_array_dict, sorted_array_dict)