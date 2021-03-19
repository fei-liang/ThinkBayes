    data = ['yellow','green']
    hypos = 'AB'

    a = MM(hypos)
    a.Update(data)

    a.Normalize()
    a.Print()