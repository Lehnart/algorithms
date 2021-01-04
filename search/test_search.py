import random
import unittest

import algorithms

MIN_INT = -1000
MAX_INT = 1000
MIN_LENGTH = 1
MAX_LENGTH = 1000


class SearchTest(unittest.TestCase):

    def setUp(self):
        self.entries = [[random.randint(MIN_INT, MAX_INT) for _ in range(n)] for n in range(MIN_LENGTH, MAX_LENGTH + 1)]

    def test_sequential_search(self):
        search_function = algorithms.sequential_search
        self._test_search(search_function)

    def test_python_search(self):
        search_function = algorithms.python_search
        self._test_search(search_function)

    def test_python_sorted_search(self):
        search_function = algorithms.python_sorted_search
        self._test_search(search_function)

    def _test_search(self, search_function):
        for i in range(len(self.entries)):
            with self.subTest(i=i):
                array = self.entries[i]

                el_index = random.randint(0, len(array) - 1)
                el = array[el_index]
                self.assertTrue(search_function(el, array))

                el = MAX_INT + 1
                self.assertFalse(search_function(el, array))

                el = random.randint(MIN_INT, MAX_INT)
                self.assertEqual(search_function(el, array), el in array)
