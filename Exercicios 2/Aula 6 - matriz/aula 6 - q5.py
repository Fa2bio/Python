#grupo Fabio da Silva Correa e João Victor Schiavo
n = int(input('Digite o número de linhas da matriz: '))
m = int(input('Digite o número de colunas da matriz: '))
matriz = []
matriz_at = []

if n == m:
    for i in range(n):
        linha = []
        for j in range(m):
            linha.append(eval(input('Digite o valor da matriz, ['+ str(i) + ',' + str(j) + ']: ')))
        matriz.append(linha)

    for i in range(len(matriz)):
        linha = []
        for j in range(len(matriz)):
            linha.append(matriz[j][i])
        matriz_at.append(linha)

    print()
    for i in range(n):
        if i == 0:
            print('Matriz original')
            print(matriz[i])
        else:
            print(matriz[i])
    print()

    for i in range(n):
        if i == 0:
            print('Matriz transposta')
            print(matriz_at[i])
        else:
            print(matriz[i])

else:
    print('A matriz não é quadrada')

