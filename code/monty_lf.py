# -*- encoding: utf-8 -*-
'''
@File    :   monty_lf.py
@Time    :   2021/03/19 11:15:14
@Author  :   Fei Liang
'''

# here put the import lib

from thinkbayes import Pmf

class Monty(Pmf):

    def __init__(self,hypos):
        Pmf.__init__(self)

        for hypo in hypos:
            self.Set(hypo,1)
        
    def Update(self,data):
        for hypo in self.Values():
            like = self.Likelihood(hypo,data)
            self.Mult(hypo,like)

    def Likelihood(self,hypo,data):
        if hypo == 'A':
            like = 0.5
        elif hypo == 'B':
            like = 0
        elif hypo == 'C':
            like = 1
        return like

if __name__ == '__main__':
    hypos = 'ABC'
    a = Monty(hypos)
    a.Update('B')
    a.Normalize()
    print(a.Prob('B'))