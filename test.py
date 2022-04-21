'''
# 拟合################################################################
    # 拟合数据
    x = np.array([20.5, 32.7, 51.0, 73.0, 95.7])
    y = np.array([76.5, 87.6, 87.3, 89.2, 103.2])


    # 用3次多项式拟合
    def ffunction(p, i):
        a = p[0]
        x_1 = p[1]
        x_2 = p[2]
        x_3 = p[3]
        return a + x_1 * i + x_2 * (i ** 2) + x_3 * (i ** 3)


    # 代价函数
    def punishment(p):
        fit_loss = 0
        for i, ty in zip(x, y):
            fit_loss += abs(ffunction(p, i) - ty)
        return fit_loss  # 与实际差距


    Ran = [[-80, 80],
           [-5, 5],
           [-5, 5],
           [-5, 5], ]
    ansyf_list, _, minf_y, minf_x = ga.ga(punishment, Ran, 50, 500,Pre=0.005)

    yvals = []
    for i, ty in zip(x, y):
        yvals.append(ffunction(minf_x, i))

    print(yvals)

    # 绘图
    plot1 = plt.plot(x, y, 's', label='original values')
    plot2 = plt.plot(x, yvals, 'r', label='polyfit values')
    plt.show()
    print('拟合系数', minf_x, '差距和', minf_y)
    plt.plot(ansyf_list)
    plt.show()

'''
