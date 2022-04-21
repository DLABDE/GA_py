"""
遗传算法(最小化)
"""
import numpy as np
import matplotlib.pyplot as plt
from GA_py import ga


def fun_2d(p):
    x = p[0]
    y = p[1]
    # return x*np.exp(-x**2-y**2)
    return 1 - (1 - y ** 5 + x ** 5) * np.exp(-x ** 2 - y ** 2)


if __name__ == '__main__':
    Ran = [[-2, 2],
           [-2, 2]]

    ansy_list, ansx_list, min_y, min_x = ga.ga(fun_2d, Ran, 10, 50)

    x1 = np.arange(Ran[0][0], Ran[0][1], 0.1)
    x2 = np.arange(Ran[1][0], Ran[1][1], 0.1)
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    xx1, xx2 = np.meshgrid(x1, x2)
    ax.plot_surface(xx1, xx2, fun_2d([xx1, xx2]), cmap=plt.cm.coolwarm, alpha=0.8)

    xx1, xx2 = np.meshgrid(min_x[0], min_x[1])
    ax.scatter(xx1, xx2, min_y, c='r')
    ax.view_init(elev=20, azim=45)
    plt.show()

    plt.plot(ansy_list)
    plt.show()

    print('Y', min_y)
    print('X', min_x)


