k = eval(input('Digite um valor para a multiplicação: '))
matriz = [] #cria a matriz

for i in range(3):
    linha = [] #cria as linhas
    for j in range(3): #preenche as linhas
        linha.append(eval(input('Digite o valor de ['+ str(i) + ',' + str(j) + ']: ')))
    matriz.append(linha) #adiciona as linhas a coluna

for i in range(3): #printa a lista em forma de matriz
    print('Matriz original: ',matriz[i])

for i in range(3): #percorre a matriz
    for j in range(3):
        if (i==j): #se as posições forem iguais, existira a diago principal, k vai multiplicar os numeros
            multiDiago = k * matriz[i][j]
            matriz[i][j] = multiDiago
print('\n')

for i in range(3): #printa a lista em forma de matriz
    print('Matriz modificada: ',matriz[i])