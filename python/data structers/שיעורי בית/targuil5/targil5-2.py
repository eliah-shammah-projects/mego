

lista = [0] * 10

num = int(input("enter a number"))

while num > 0:

    temp = num % 10
    for i in range (10):
        if temp == i:
            lista[i] += 1
    num //= 10

for y in range (10):
    if lista[y] != 0:
        print (f"the number {y} appears {lista[y]} time/s")

