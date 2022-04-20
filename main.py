"""
遗传算法(最小化)
"""
import numpy as np
import matplotlib.pyplot as plt

from GA_py import ga


def fun(x):
    return -abs(np.sin(x) / ((abs(x) / 10 - x / 30) + 0.1)) + 0.01*x+5


if __name__ == '__main__':
    Ran = [-60, 60]
    t = np.arange(Ran[0], Ran[1], 0.1)
    y1 = fun(t)
    plt.plot(t, y1)
    plt.show()

    ansy_list, ansx_list, min_y, min_x = ga.ga(fun, Ran, 10, 40)

    print('Y', min_y)
    print('X', min_x)
    print('re', fun(min_x))
    plt.plot(ansy_list)
    plt.show()
