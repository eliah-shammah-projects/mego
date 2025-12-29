


mat = [[0 for i in range(6)] for y in range(5)]

count = 1

for i in range (5):

    if i % 2 == 0: 
      for j in range (6):

          mat[i][j] = count 
          count += 1
    else:
       for j in range (len(mat[i]) - 1, -1, -1):
           
          mat[i][j] = count 
          count += 1
    
for i in range (5):

   print (mat[i])

 
       







        

