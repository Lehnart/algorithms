import random
import unittest

MIN_X = -1000.
MAX_X = 1000.
MIN_Y = -1000.
MAX_Y = 1000.

MIN_N_POINTS = 3
MAX_N_POINTS = 1000


class InterpolationTest(unittest.TestCase):

    def setUp(self):
        self.xs_list = [[random.uniform(MIN_X, MAX_X) for _ in range(n)] for n in range(MIN_N_POINTS, MAX_N_POINTS + 1)]
        self.ys_list = [[random.uniform(MIN_Y, MAX_Y) for _ in range(n)] for n in range(MIN_N_POINTS, MAX_N_POINTS + 1)]
        for xs in self.xs_list:
            xs.sort()

    def _test_interpol(self, interpol_function):
        for i in range(len(self.xs_list)):
            with self.subTest(i=i):
                xs = self.xs_list[i]
                ys = self.ys_list[i]

                for j in range(len(xs)):
                    x, y = xs[j], ys[j]
                    y_interpol = interpol_function(x)
                    self.assertAlmostEqual(y, y_interpol)

                    if j == 0:
                        continue
                    for k in range(1, 10):
                        self.assertIsInstance(interpol_function(x + 0.1 * (xs[j + 1] - xs[j])), float)