

amount = []
month = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dec"]

for i in range (12):

    a = int(input(f"enter the amount of month {month[i]}"))
    amount.append(a)

maxList=[]
minList=[]

maxIndex = 0
minIndex = 0

for a in range (len(amount)):
    if amount[a] > amount[maxIndex]:
        maxIndex=a
        maxList=[month[a]]
    elif amount[a]==amount[maxIndex]:
        maxList.append(month[a])
    if amount[a] < amount[minIndex]:
        maxIndex=a
        minList=[month[a]]
    elif amount[a]==amount[minIndex]:
        minList.append(month[a])

print ("The max:")
print (maxList)
print ("The min:")
print (minList)