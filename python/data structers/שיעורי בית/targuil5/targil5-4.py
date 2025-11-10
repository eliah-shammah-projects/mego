

bin = int(input("enter your number "))

while True:  
  if len(str(bin)) == 12:
    break 
  else:
    print ("the length must be 12 digits")
    bin = int(input("enter your number "))

lis = [0] * 13

count = 0 

for i in range (12):
  
  temp = bin % 10
  if temp == 1:
    count += 1
  else:
    lis[count] += 1
    count = 0
  bin //= 0

lis[count] += 1


for y in range (1, 13):
  
  if lis[y] != 0:
    print ("sequence of {y} numbers apppears {lis[y]} time/s")
  
  
  
  


