

def findMissing(l:list[int],n:int)->int:
    
    if n <= 2:
        print ("the list contains only one number or less")
        return 0
    else:
       for i in range(1, n + 1):
           if i not in l:   
            return i

