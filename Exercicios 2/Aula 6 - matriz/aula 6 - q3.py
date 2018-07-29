#grupo Fabio da Silva Correa e João Victor Schiavo
linhas_a = int(input("Digite quantas linhas você quer para a matriz A: "))
colunas_a = int(input("Digite quantas colunas você quer para a matriz A: "))

matriz_a = []
for lin in range(linhas_a):
    linha = []
    for col in range(colunas_a):
        linha.append(eval(input("Digite o item da posição (" + str(lin + 1) + ", " + str(col + 1) + ") da matriz A: ")))
    matriz_a.append(linha)
for i in range(len(matriz_a)):
    print(matriz_a[i])
print()

# Pede as dimensões da matriz B
linhas_b = int(input("Digite quantas linhas você quer para a matriz B: "))
colunas_b = int(input("Digite quantas colunas você quer para a matriz B: "))

# Cria B por input
matriz_b = []
for lin in range(linhas_b):
    linha = []
    for col in range(colunas_b):
        linha.append(eval(input("Digite o item da posição (" + str(lin + 1) + ", " + str(col + 1) + ") da matriz B: ")))
    matriz_b.append(linha)
for i in range(len(matriz_b)):
    print(matriz_b[i])
print()

if colunas_a == linhas_b:
    matriz_c = []
    for i in range(linhas_a):
        matriz_c.append([0] * colunas_b)

    lin_a = col_a = lin_b = col_b = 0

    while lin_a < linhas_a or col_a < colunas_a or lin_b < linhas_b or col_b < colunas_b:
        soma = 0
        for n_somas in range(colunas_a):
            soma += (matriz_a[lin_a][col_a] * matriz_b[lin_b][col_b])
            col_a += 1
            lin_b += 1
        matriz_c[lin_a][col_b] = soma

        col_b += 1
        if col_b < colunas_b:
            col_a = 0
            lin_b = 0
        else:
            lin_a += 1
            if lin_a < linhas_a:
                col_a = 0
                col_b = 0
                lin_b = 0

    for i in range(len(matriz_c)):
        print(matriz_c[i])

else:
    print("Não é possível multiplicar as duas matrizes.")