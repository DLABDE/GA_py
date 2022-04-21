"""
遗传算法(最小化)
"""
import numpy as np
import matplotlib.pyplot as plt

from GA_py import ga


def fun(x):
    return -abs(np.sin(x) / ((abs(x) / 10 - x / 30) + 0.1)) + 0.05*x+5.16


if __name__ == '__main__':
    Ran = [-90, 20]
    ansy_list, ansx_list, min_y, min_x = ga.ga(fun, Ran, 15, 50)

    t = np.arange(Ran[0], Ran[1], 0.1)
    y1 = fun(t)
    plt.plot(t, y1)
    plt.plot(min_x, min_y, 'ro')
    plt.show()
    print('Y', min_y)
    print('X', min_x)
    plt.plot(ansy_list)
    plt.show()
