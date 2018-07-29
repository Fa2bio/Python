#grupo Fabio da Silva Correa e João Victor Schiavo
matriz_A = []
matriz_B = []
matriz_C = []

for i in range(2):
    linha = [] #cria as linhas
    for j in range(2): #preenche as linhas
        linha.append(eval(input('Digite o valor da matriz A, ['+ str(i) + ',' + str(j) + ']: ')))
    matriz_A.append(linha) #adiciona as linhas a coluna

for i in range(2):
    linha = [] #cria as linhas
    for j in range(2): #preenche as linhas
        linha.append(eval(input('Digite o valor da matriz B, ['+ str(i) + ',' + str(j) + ']: ')))
    matriz_B.append(linha) #adiciona as linhas a coluna

for i in range(2):
    matriz_C.append([0]*2)

for i in range(2):
    for j in range(2):
        matriz_C[i][j] = matriz_A[i][j] + matriz_B[i][j]

for i in range(2):
    print ('Matriz C:',matriz_C[i])
