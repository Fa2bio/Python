r = int(input())
x = input().split()
for i in range(r-1):
    x[i] = int(x[i])
a = True
cont = 0
while a:
    cont +=1
    a = False
    for j in x:
        if cont == j:
            a = True
print(cont)