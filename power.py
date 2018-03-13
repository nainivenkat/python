def power(x,y):
    if y ==0:
        return 1

    if y >0:
        if y % 2 == 0:
            return power(x,y/2)*power(x,y/2)
        else:
            return x*power(x,y/2)*power(x,y/2)
    else:
        y = abs(y)
        if y % 2 == 0:
            return 1.0/(power(x,y/2)*power(x,y/2))
        else:
            return 1.0/(x*power(x,y/2)*power(x,y/2))
        



print power(2,-4)
