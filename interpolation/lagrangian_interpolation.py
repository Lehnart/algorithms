from typing import List

import matplotlib.pyplot as plt


def lagrange_polynom_at_i(xs: List, i: int, yi: float = 1.):
    xi = xs[i]

    def p(x):
        p = 1.
        for j,xj in enumerate(xs):
            if i == j : continue
            p *= (x - xj) / (xi - xj)
        p *= yi
        return p

    return p


def lagrange_polynom(xs: List, ys: List):
    ls = [lagrange_polynom_at_i(xs, i, ys[i]) for i in range(len(xs))]

    def p(x):
        s = 0
        for i in range(len(ys)):
            s += ls[i](x)
        return s

    return p


if __name__ == "__main__":
    xs = [0, 1, 2, 3, 4]
    ys = [1, 2, 3, 2, 1]

    f,ls = lagrange_polynom(xs, ys)
    Xs = [x * 0.1 for x in range(0, 50)]
    Ys = [f(x) for x in Xs]

    plt.plot(Xs, Ys)
    plt.show()
