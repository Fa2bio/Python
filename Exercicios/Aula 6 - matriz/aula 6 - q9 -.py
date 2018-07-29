matriz = []
maior = 0
menor = 0
linha_maior = 0
coluna_maior = 0
linha_menor = 0
coluna_menor = 0

for i in range(6):
    linha = []
    for j in range(3):
        num = eval(input('Digite um número real,[' + str(i) + ',' + str(j) + ']: '))
        linha.append(num)
        if num > maior:
            maior = num
            menor = num
            linha_maior = i
            coluna_maior = j
    matriz.append(linha)

for i in range(6):
    for j in range(3):
        if matriz[i][j] < menor:
            menor = matriz[i][j]
            linha_menor = i
            coluna_menor = j

for i in range(6):
    print(matriz[i])
print('\n')

print('O maior número é', maior,'e esta na posição','[',linha_maior,']','[',coluna_maior,']')
print('O menor número é', menor,'e esta na posição','[',linha_menor,']','[',coluna_menor,']')
