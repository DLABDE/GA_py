"""
遗传算法(最小化)
"""
import numpy as np
import matplotlib.pyplot as plt
from GA_py import ga


def fun_1d(p):
    x = p[0]
    return -abs(np.sin(x) / ((abs(x) / 10 - x / 30) + 0.1)) + 0.05 * x + 5.16


def fun_2d(p):
    x = p[0]
    y = p[1]
    # return x*np.exp(-x**2-y**2)
    return 1 - (1 - y ** 5 + x ** 5) * np.exp(-x ** 2 - y ** 2)


if __name__ == '__main__':
    # 单参数示例
    Ran = [[-90, 20]]  # 单参数，取值[-90,20]
    ansy_list, ansx_list, min_y, min_x = ga.ga(fun_1d, Ran, 15, 50)  # 初始群体15，迭代次数50
    # 绘制函数图像
    t = np.arange(-90,20, 0.1)
    y1 = fun_1d(t)
    plt.plot(t, y1)
    plt.plot(min_x[0], min_y, 'ro')  # 最优点
    plt.show()
    # 最佳解
    print('Y', min_y)
    print('X', min_x)
    # 运行过程
    plt.plot(ansy_list)
    plt.show()

    # 双参数示例
    Ran = [[-2, 2],  # 两个参数与取值范围
           [-2, 2]]
    ansy2_list, ansx2_list, min2_y, min2_x = ga.ga(fun_2d, Ran, 10, 50)  # 初始群体10，迭代次数50

    # 绘制图像
    x1 = np.arange(Ran[0][0], Ran[0][1], 0.1)
    x2 = np.arange(Ran[1][0], Ran[1][1], 0.1)
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    xx1, xx2 = np.meshgrid(x1, x2)
    ax.plot_surface(xx1, xx2, fun_2d([xx1, xx2]), cmap=plt.cm.coolwarm, alpha=0.8)
    xx1, xx2 = np.meshgrid(min2_x[0], min2_x[1])
    ax.scatter(xx1, xx2, min2_y, c='r')  # 最佳点
    ax.view_init(elev=20, azim=45)
    plt.show()
    # 运行过程
    plt.plot(ansy2_list)
    plt.show()
    # 最佳解
    print('Y', min2_y)
    print('X', min2_x)
