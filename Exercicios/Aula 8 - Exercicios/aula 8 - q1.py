def maior(matriz):
    vet_maior = []
    for i in range(len(matriz)):
        maior_num = 0
        for j in range(2):
            if matriz[i][j] > maior_num:
                maior_num = matriz[i][j]
        vet_maior.append(maior_num)
    return vet_maior

def multi():
    x = maior(matriz)
    soma = 0
    for i in range(len(x)):
        if soma == 0:
            soma = x[i]
        else:
            soma *= x[i]

    return soma

n = int(input('Quantos pares de números você deseja adicionar ?: '))
matriz = []
for i in range(n):
    linha = []
    for j in range(2):
        linha.append(eval(input('Digite um número: ')))
    matriz.append(linha)

print('A multiplicação dos maiores valores é:',multi())