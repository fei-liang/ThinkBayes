# -*- encoding: utf-8 -*-
'''
@File    :   cookie3.py
@Time    :   2021/03/19 10:45:05
@Author  :   Fei Liang
'''

# here put the import lib
from thinkbayes import Pmf


class Cookie(Pmf):

    def __init__(self,hypos):
        Pmf.__init__(self)

        for hypo in hypos:
            self.Set(hypo,1)
    
    def Update(self, data):
        for hypo in self.Values():
            like = self.Likelihood(hypo,data)
            self.Mult(hypo,like)

    mixs = {'bowl_1':{'vanilla':0.75,'chocolate':0.25},
    'bowl_2':{'vanilla':0.5,'chocolate':0.5}}


    def Likelihood(self,hypo,data):
        like = self.mixs.get(hypo).get(data)
        return like


if __name__ == '__main__':
    hypos = ['bowl_1','bowl_2']
    a = Cookie(hypos)
    picklist = ['vanilla','vanilla','chocolate','vanilla']

    for i,pick in zip(range(len(picklist)),picklist):
        a.Update(pick)
        # a.Normalize()
        # print(i,a.Prob('bowl_1'))

    a.Normalize()
    print(a.Prob('bowl_1'))

    