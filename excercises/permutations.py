def permutations(lst):
    if len(lst) == 1:
        return[lst]
    l = []
    for i in range(len(lst)):
        m = lst[i]
        remlst = lst[:i]+lst[i+1:]
        for p in permutations(remlst):
            l.append([m]+p)
    return l

data = list('1234')
for p in permutations(data):
    print p
