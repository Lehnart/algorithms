from random import randint
from typing import List

import matplotlib.pyplot as plt


def lagrange_polynom_at_i(xs: List, i: int, yi: float = 1.):
    xi = xs[i]

    def p(x):
        p = 1.
        for j, xj in enumerate(xs):
            if i == j: continue
            p *= (x - xj) / (xi - xj)
        p *= yi
        return p

    return p


def lagrange_polynom(xs: List, ys: List):
    test_xs = xs[:]
    test_xs.sort()
    if test_xs != xs:
        raise Exception("xs need to be sorted. ", xs)

    ls = [lagrange_polynom_at_i(xs, i, ys[i]) for i in range(len(xs))]

    def p(x):
        s = 0
        for i in range(len(ys)):
            s += ls[i](x)
        return s

    return p


def lagrange_interval_polynom(xs: List, ys: List, indices: List[int] = None):
    """
    :param xs:
    :param ys:
    :param indices: index where to split the xs abd ys to build the intervals
    :return:
    """

    if indices is None:
        n_indices = randint(1, len(xs))
        indices = [randint(0, len(xs) - 1) for _ in range(n_indices)]

    inds = [0, *indices, len(xs) - 1]
    inds = list(set(inds))
    inds.sort()

    if inds[0] != 0 or inds[-1] != len(xs) - 1:
        raise Exception("interval indices are not valids. Here are the index: ", inds)

    ls = []
    for i in range(len(inds) - 1):
        i0 = inds[i]
        i1 = inds[i + 1]

        xis = xs[i0:i1 + 1]
        yis = ys[i0:i1 + 1]
        xMin = float('-inf') if i0 == 0 else xis[0]
        xMax = float('inf') if i1 == len(xs) - 1 else xis[-1]
        ls.append((xMin, xMax, lagrange_polynom(xis, yis)))

    def p(x):
        for l in ls:
            if l[1] > x >= l[0]:
                return l[2](x)
        return None

    return p


if __name__ == "__main__":
    xs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    ys = [1, 2, 3, 2, 1, 0, 1, 2, 3, 4]

    f = lagrange_interval_polynom(xs, ys, [1,4])
    Xs = [x * 0.1 for x in range(0, 50)]
    Ys = [f(x) for x in Xs]

    plt.plot(Xs, Ys)
    plt.show()
