def hanoi(n,cont):
    if n == 1:
        cont += 1
        return cont
    cont += 2*hanoi(n-1,cont)+1
    return cont

loop = 1
while True:
    n = int(input())
    if n == 0:
        break
    else:
        cont = 0
        print("Teste",loop)
        print(hanoi(n,cont))
        loop += 1
        print()