#grupo Fabio da Silva Correa e João Victor Schiavo
matriz = []
maior = 0
menor = 0
linha_maior = 0
coluna_maior = 0
linha_menor = 0
coluna_menor = 0

#acha a o maior número e sua respectiva posição
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

#acha o menor número e sua respectiva posição
for i in range(6):
    for j in range(3):
        if matriz[i][j] < menor:
            menor = matriz[i][j]
            linha_menor = i
            coluna_menor = j

for i in range(6):
    print(matriz[i])
print()

print('O maior número é', maior,'e esta na posição:','['+ str(linha_maior) +']'+'['+ str(coluna_maior) +']')
print('O menor número é', menor,'e esta na posição:','['+ str(linha_menor) +']'+'['+ str(coluna_menor) +']')
