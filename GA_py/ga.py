"""
遗传算法(最小化)
"""
import random
import math

GA_box = list()  # 包含所有存活个体
Total = None  # 暂存活数目
ANS_Y = None  # 最佳值
ANS_X = list()  # 最佳解


def ga(fun_cost, Ran, Box_num, Times_num, Pre=0.1, Cross=0.68, Mut_rat=0.05):
    """
    遗传算法
    :param fun_cost: 损失函数
    :param Ran: 各个参数的解算范围[[L1,H1],[L2,H2],,]
    :param Box_num: 初始个体数目
    :param Times_num: 迭代次数
    :param Pre: 解算精度
    :param Cross: 交叉变异概率
    :param Mut_rat: 基因突变概率
    :return: [Y历史list,X历史list[list],最佳值,最佳解[list]]
    """
    global Total
    Total = Box_num

    class Biology(object):
        """
        GA中的个体
        """

        def __init__(self, name, gene, mut):
            """
            初始化个体信息
            :param name: 个体索引，在list中的位置
            :param gene: 基因(二进制字符串)[是list,与参数对应]
            :param mut: 变异概率(0-1)
            """
            self.name = name
            self.gene = gene
            self.mut = mut
            self.loss = None  # 损失
            self.ans = list()  # 解算的x

        def delete(self):
            """
            个体凋亡，更新其他个体索引
            """
            global Total
            for i in GA_box[self.name + 1:]:  # 遍历在本个体后的每一个个体
                i.name = i.name - 1
            GA_box.pop(self.name)  # 删除自己
            Total = Total - 1  # 现存总数减一

        def up_loss(self):
            """
            更新损失
            """
            self.ans = []
            for i in range(len(self.gene)):  # 遍历染色体
                x = int(self.gene[i], 2)
                max = '1' * len(self.gene[i])
                self.ans.append(x / int(max, 2) * abs(Ran[i][1] - Ran[i][0]) + min(Ran[i]))  # 解算基因
            self.loss = fun_cost(self.ans)

        def bio_mut(self):
            """
            基因突变
            """
            after_lis = []
            for i in self.gene:
                lis = list(i)  # 取每一条染色体
                for k in range(len(lis)):
                    if random.random() < self.mut:
                        lis[k] = '1' if lis[k] == '0' else '0' if lis[k] == '1' else '1'
                after_lis.append(''.join(lis))
            self.gene = after_lis

    def gene_hlong():
        """
        计算基因长度
        :return: list()每个染色体对应一个长度
        """
        hlong = []
        def get_long(diff):
            return int(math.log(diff / Pre, 2) + 0.5)  # 向上取整

        for i in range(len(Ran)):
            hlong.append(get_long(abs(Ran[i][1] - Ran[i][0])))
        return hlong

    def gene_init():
        """
        返回随机基因
        :return: list()每个参数对应一个染色体
        """
        gene = []
        for i in gene_hlong():
            ge = ''
            for k in range(i):
                ge += random.choice(['0', '1'])
            gene.append(ge)
        return gene

    def up_ans():
        """
        更新最佳值、最佳解
        """
        global ANS_Y, ANS_X
        ansy = list()
        for i in GA_box:
            ansy.append(i.loss)
        ANS_Y = min(ansy)
        ANS_X = GA_box[ansy.index(ANS_Y)].ans

    def cross_var():
        """
        交叉变异
        """
        global Total
        after_ones = []
        after_twos = []
        ones = random.choice(GA_box).gene
        twos = random.choice(GA_box).gene
        for i in range(len(ones)):  # 遍历个体每一条染色体
            one = list(ones[i])
            two = list(twos[i])
            k = random.randint(1, len(one) - 1)  # 随机交叉节点
            inter = one[k:]
            one[k:] = two[k:]
            two[k:] = inter

            one_str = ''.join(one)
            two_str = ''.join(two)
            after_ones.append(one_str)
            after_twos.append(two_str)
        GA_box.append(Biology(Total, after_ones, Mut_rat))
        GA_box.append(Biology(Total + 1, after_twos, Mut_rat))
        Total = Total + 2

    def keil_some():
        """
        射杀低水平群体，维持种群数量
        """
        loss_sum = 0
        for i in GA_box:
            loss_sum += i.loss
        for i in GA_box:
            if i.loss > (loss_sum / Total):
                i.delete()
            if Total > (5 * Box_num):  # 种群数量过多时，防止种群爆炸
                if random.random() < 0.632:  # 1-1/e
                    i.delete()

    ansy_list = list()
    ansx_list = list()
    for i in range(Box_num):  # 初始化个体
        GA_box.append(Biology(i, gene_init(), Mut_rat))
        GA_box[i].up_loss()
    up_ans()
    for i in range(1, Times_num + 1):  # 总迭代
        for k in range(int(Total / 2 + 0.5)):  # 随机两两匹配，准备交叉变异
            if random.random() < Cross:
                cross_var()
        for m in range(Total):
            GA_box[m].bio_mut()  # 基因突变
            GA_box[m].up_loss()  # 计算损失
        up_ans()
        keil_some()
        ansy_list.append(ANS_Y)
        ansx_list.append(ANS_X)
        min_y = min(ansy_list)
        min_x = ansx_list[ansy_list.index(min_y)]

    return ansy_list, ansx_list, min_y, min_x
