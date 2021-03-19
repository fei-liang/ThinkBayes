# -*- encoding: utf-8 -*-
'''
@File    :   dice_lf.py
@Time    :   2021/03/19 16:17:08
@Author  :   Fei Liang
'''

# here put the import lib

from thinkbayes import Suite

class Dice(Suite):
    def Likelihood(self,hypo,data):
        if hypo < data:
            like = 0
        else:
            like = 1/hypo
        return like

if __name__ == '__main__':
    a = Dice([4,6,8,10,14])

    # roll 6
    a.Update(6)
    a.Print()

    # roll several times
    rolllist = [5,6,6,8,7]

    for roll in rolllist:
        a.Update(roll)
        print('the roll number is %s' %roll)
        a.Print()

