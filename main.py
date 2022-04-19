"""
遗传算法(最小化)
"""
import random
import math
import numpy as np
import matplotlib.pyplot as plt

Ran = [-100, 100]  # 解算范围
Pre = 0.1  # 解算精度

Times = 30  # 迭代次数
Box_num = 10  # 个体数目
Cross = 0.4  # 交叉变异概率
Mut_rat = 0.01  # 基因突变概率

GA_box = list()  # 包含所有存活个体
ANS = 0  # 最佳解
Total = Box_num  # 现存总数

def fun_cost(x):
    return (0.5*x**2*np.sin(x))

class Biology(object):
    """
    GA中的个体
    """

    def __init__(self, name, gene, mut, getion):
        """
        初始化个体信息
        :param name: 个体索引，在list中的位置
        :param gene: 基因(b)
        :param mut: 变异概率(0-1)
        :param getion:第几代(int)
        """
        self.name = name
        self.gene = gene
        self.mut = mut
        self.getion = getion
        self.loss = 100000

    def delete(self):
        """
        个体凋亡，更新其他个体索引
        """
        global GA_box, Total
        for i in GA_box[self.name + 1:]:  # 遍历在本个体后的每一个个体
            i.name = i.name - 1
        GA_box.pop(self.name)
        Total = Total - 1

    def up_loss(self, fun_cost):
        """
        更新损失
        :param fun_cost: 损失函数
        :return:
        """
        self.loss = fun_cost(self.gene)

    def bio_mut(self):
        """
        基因突变
        """
        lis = list(self.gene)
        for i in range(len(lis)):
            if random.random() < self.mut:
                lis[i] = '1' if lis[i] == '0' else '0' if lis[i] == '1' else '1'
        self.gene = ''.join(lis)


def cost(gene):
    """
    解算损失
    :param gene: 基因(string)
    :return: 损失
    """
    x = int(gene, 2) + min(Ran)
    return fun_cost(x)


def gene_hlong():
    """
    计算基因长度(暂时只有单变量)
    """
    global Ran, Pre
    diff = abs(Ran[1] - Ran[0])
    return int(math.log(diff / Pre, 2) + 0.5)  # 向上取整


def gene_init():
    """
    返回随机基因
    """
    gene = ''
    for i in range(gene_hlong()):
        gene += random.choice(['0', '1'])
    return gene


def ga_init():
    """
    GA池初始化
    """
    global GA_box, Box_num

    # 初始化个体
    for i in range(Box_num):
        GA_box.append(Biology(i, gene_init(), Mut_rat, 0))
        GA_box[i].up_loss(cost)
    up_ans()


def up_ans():
    """
    更新最佳个体和最佳值
    """
    global ANS, GA_box
    ans = list()
    for i in GA_box:
        ans.append(i.loss)
    ANS = min(ans)


def cross_var(i):
    """
    交叉变异
    :param i: 目前代数
    """
    global GA_box, Total
    one = list(random.choice(GA_box).gene)
    two = list(random.choice(GA_box).gene)
    k = random.randint(1, gene_hlong() - 1)  # 随机交叉节点
    inter = one[k:]
    one[k:] = two[k:]
    two[k:] = inter
    GA_box.append(Biology(Total, ''.join(one), Mut_rat, i))
    GA_box.append(Biology(Total + 1, ''.join(two), Mut_rat, i))
    Total = Total + 2



if __name__ == '__main__':

    t = np.arange(Ran[0],Ran[1],0.1)
    y1 = fun_cost(t)
    plt.plot(t, y1)
    plt.show()

    ans_list = list()
    ga_init()
    for i in range(1, Times + 1):  # 总迭代
        # 随机两两匹配，准备交叉变异
        for k in range(int(Total / 2 + 0.5)):
            if random.random() < Cross:
                cross_var(i)
        # 计算损失
        for m in range(Total):
            GA_box[m].up_loss(cost)
        up_ans()

        # 基因突变
        for m in range(Total):
            GA_box[m].bio_mut()
        up_ans()

        # # 射杀低水平群体，维持种群数量

        ans_list.append(ANS)
    print(min(ans_list))
    plt.plot(ans_list)
    plt.show()
