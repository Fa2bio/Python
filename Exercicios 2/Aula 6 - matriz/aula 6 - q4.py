#grupo Fabio da Silva Correa e João Victor Schiavo
matriz = []
matriz_aux = []
linha_1 = 0
linha_2 = 0
linha_3 = 0

for i in range(3):
    linha = []
    for j in range(3):
        linha.append(eval(input('Digite um numero,['+ str(i) + ',' + str(j) + ']: ')))
    matriz.append(linha)

for i in range(3):
    for j in range(3):
        if i == 0:
            linha_1 += matriz[i][j]
        elif i == 1:
            linha_2 += matriz[i][j]
        else:
            linha_3 += matriz[i][j]

if linha_1 > linha_2 and linha_1 > linha_3:
    print()
    for a in range(3):
        print(matriz[a])
    print()

    for i in range(3):
        for j in range(3):
            if i == 0:
                matriz_aux.append(matriz[i][j])
    print('A linha da maior soma é a linha 1:',matriz_aux)
    print('A linha de maior soma vale:', linha_1)

elif linha_2 > linha_1 and linha_2 > linha_3:
    print()
    for a in range(3):
        print(matriz[a])

    print()
    for i in range(3):
        for j in range(3):
            if i == 1:
                matriz_aux.append(matriz[i][j])
    print('A linha da maior soma é a linha 2:',matriz_aux)
    print('A linha de maior soma vale:',linha_2)

else:
    print()
    for a in range(3):
        print(matriz[a])
    print()

    for i in range(3):
        for j in range(3):
            if i == 2:
                matriz_aux.append(matriz[i][j])
    print('A linha da maior soma é a linha 3:',matriz_aux)
    print('A linha de maior soma vale:',linha_3)