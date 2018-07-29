def menor(custo):
    menor = custo[0]
    for i in range(len(custo)):
        if custo[i] < menor:
            menor = custo[i]
    return menor

um = int(input())
dois = int(input())
tres = int(input())

andares = [um,dois,tres]
custo = []

for j in range(len(andares)):
    contador = 0
    if j == 0:
        contador += andares[j+1]*2
        contador += andares[j+2]*4
    elif j == 1:
        contador += andares[j-j]*2
        contador += andares[j+1]*2
    else:
        contador += andares[j-2]*4
        contador += andares[j-1]*2

    custo.append(contador)

print(menor(custo))