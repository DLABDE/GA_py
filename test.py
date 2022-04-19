import random

class Solution(object):
    def __init__(self, i):
        self.i = i
        # print('创建'+str(i))

    def play(self):
        print(self.i)


class solve(Solution):
    def __init__(self):
        pass

    def init(self, name, pag):
        self.name = name
        self.pag = pag

    def play(self):
        print(Solution.i)


if __name__ == '__main__':
    print(int('1001',2))
