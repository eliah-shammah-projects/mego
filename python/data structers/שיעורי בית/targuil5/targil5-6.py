def arithmeticMean(a:list[int])->float:

    s = 0

    for i in a:
        s += i
    
    n = len(a)

    return float(s / n)


def geomrtricMean(a:list[int])->float:


    s = 1
    n = len(a)

    for i in a:
        s  *= i

    return float(s ** (1/n))

    
def harmonicMean(a:list[int])->float:

    n = len(a)
    s = 0
    for i in a:
        s += 1/ i

    return float(n / s)

def i_shivion (l:list[int]):

    a = arithmeticMean(l)
    b = geomrtricMean(l)
    c = harmonicMean (l)


    if a >= b >= c: 
        return True
    else:
        return False

    





