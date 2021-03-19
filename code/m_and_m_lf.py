# -*- encoding: utf-8 -*-
'''
@File    :   m_and_m_lf.py
@Time    :   2021/03/19 14:38:53
@Author  :   Fei Liang
'''

# here put the import lib
from thinkbayes import Suite

"""
我觉得这一道题应该是说，从袋中拿球的顺序不变，每次从中拿出两个球，然后根据球的颜色来判断第一个袋子是mix94，还是mix96
所以data是（‘yellow’，‘green’），（‘green’，‘red’）构成的列表
我写的比作者写的好！！！很容易复用，逻辑很好理解啊
"""


class MM(Suite):

    mix94 = dict(brown=30,
                 yellow=20,
                 red=20,
                 green=10,
                 orange=10,
                 tan=10,
                 blue=0)

    mix96 = dict(blue=24,
                 green=20,
                 orange=16,
                 yellow=14,
                 red=13,
                 brown=13,
                 tan=0)

    hypoA = dict(bag1=mix94, bag2=mix96)
    hypoB = dict(bag1=mix96, bag2=mix94)

    hypotheses = dict(A=hypoA, B=hypoB)

    def Likelihood(self,hypo,data):
        first = data[0]
        second = data[1]
        like = self.hypotheses.get(hypo).get('bag1').get(first)*self.hypotheses.get(hypo).get('bag2').get(second)
        return like



if __name__ == '__main__':

    datalist = [['yellow','green'],['red','green'],['orange','green']]
    hypos = 'AB'
    # print(data[1])

    a = MM(hypos)
    for data in datalist:
        a.Update(data)
        a.Normalize()
        a.Print()