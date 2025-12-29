
arr = [8,9,0,7,13,45,6,4,66]
new = list(map(lambda x: x*3, list(filter(lambda x: x >= 5 and x <= 10, arr))))
print (new)