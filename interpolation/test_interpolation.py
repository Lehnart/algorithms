import random
import unittest
import pygame
from interpolation import lagrangian_interpolation

MIN_X = -1000.
MAX_X = 1000.
MIN_Y = -1000.
MAX_Y = 1000.

MIN_N_POINTS = 3
MAX_N_POINTS = 75


class InterpolationTest(unittest.TestCase):

    def setUp(self):
        self.xs_list = [[random.uniform(MIN_X, MAX_X) for _ in range(n)] for n in range(MIN_N_POINTS, MAX_N_POINTS + 1)]
        self.ys_list = [[random.uniform(MIN_Y, MAX_Y) for _ in range(n)] for n in range(MIN_N_POINTS, MAX_N_POINTS + 1)]
        for xs in self.xs_list:
            xs.sort()

    def test_lagrangian_interpolation(self):
        interpolation_function = lagrangian_interpolation.lagrange_polynom
        self._test_interpol(interpolation_function)

    def test_lagrangian_interval_interpolation(self):
        interpolation_function = lagrangian_interpolation.lagrange_interval_polynom
        self._test_interpol(interpolation_function)

    def _test_interpol(self, interpol_method):

        for i in range(len(self.xs_list)):
            with self.subTest(i=i):
                xs = self.xs_list[i]
                ys = self.ys_list[i]
                interpol_function = interpol_method(xs,ys)
                for j in range(len(xs)):
                    x, y = xs[j], ys[j]
                    y_interpol = interpol_function(x)
                    self.assertAlmostEqual(y, y_interpol)

                for k in range(1, 10):
                    rx = xs[0]+ (random.random()*(xs[-1]-xs[0]))
                    self.assertIsInstance(interpol_function(rx), float)