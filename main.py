"""
遗传算法(最小化)
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from GA_py import ga


def fun(p):
    print(len(p))
    x=p[0]
    y=p[1]
    return -(1 - y ** 5 + x ** 5) * np.exp(-x ** 2 - y ** 2)


if __name__ == '__main__':
    Ran = [[-2, 2],
           [-2, 2]]

    # ansy_list, ansx_list, min_y, min_x = ga.ga(fun, Ran, 15, 50)

    x1 = np.arange(Ran[0][0], Ran[0][1], 0.1)
    x2 = np.arange(Ran[1][0], Ran[1][1], 0.1)
    fig = plt.figure()
    ax = Axes3D(fig)
    xx1, xx2 = np.meshgrid(x1, x2)
    ax.plot_surface(xx1, xx2, fun([xx1, xx2]))
    plt.show()

'''    print('Y', min_y)
    print('X', min_x)
    plt.plot(ansy_list)
    plt.show()'''
