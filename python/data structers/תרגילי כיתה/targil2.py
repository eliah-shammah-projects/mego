

mat = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]


for i in range (4):
    for y in range (4):
        print (mat[i][y], end = " ")
    print ("")

print ("______________________")
for a in range (4):
    print (mat[a][a], end = " ")
print ("")
print ("______________________")
count = 0
for b in range( len(mat) - 1, -1 , -1):
    print (mat[count][b], end = " ")
    count += 1






