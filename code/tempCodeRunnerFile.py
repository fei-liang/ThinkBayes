if __name__ == '__main__':
    hypos = 'ABC'
    a = Monty(hypos)
    a.Update('B')
    a.Normalize()
    print(a.Prob('A'))