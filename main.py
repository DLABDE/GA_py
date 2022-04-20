"""
遗传算法(最小化)
"""
import numpy as np
import matplotlib.pyplot as plt

from GA_py import ga


def fun(x):
    return -abs(np.sin(x) / ((abs(x) / 10 - x / 30) + 0.1))

if __name__ == '__main__':
    Ran = [-15, 15]
    t = np.arange(Ran[0], Ran[1], 0.1)
    y1 = fun(t)
    plt.plot(t, y1)
    plt.show()

    ansy_list, ansx_list = ga.ga(fun, Ran, 50, 30)

    print('Y', min(ansy_list))
    print('X', min(ansx_list))
    print('re', fun(min(ansx_list)))
    plt.plot(ansy_list)
    plt.show()
