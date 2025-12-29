
def bar (l):
    return sum(bar)

def _bar (n):
    li = []
    for i in range (n+1):
        li.append(i)
    return li

if __name__=="__name__":
    a1 = [1,2,3]
    print (bar(a1))
    a2 = _bar(4)
    print (_bar(a2))



