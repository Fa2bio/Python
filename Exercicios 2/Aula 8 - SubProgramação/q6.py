__author__ = 'Fabio'
def faltas(matriz):
    cont = 0
    for i in range(len(matriz)):
        for j in range(len(linha)):
            for k in range(len(aux)):
                if j == 2:
                    cont += matriz[i][j][k]
    return cont

def mais_faltas(matriz,linha,aux):
    nome = []
    maior = 0
    x = []
    for i in range(len(matriz)):
        for j in range(len(linha)):
            for k in range(len(aux)):
                if j == 2:
                    if matriz[i][j][k] > maior:
                        maior = matriz[i][j][k]

    print('\n Times que fizeram mais faltas')
    for a in range(len(matriz)):
        x = matriz[a]
        for b in range(len(x)):
                if x[2][0] == maior:
                    nome = x[0].upper()
                elif x[2][1] == maior:
                    nome = x[1].upper()
        print(nome)

def menos_faltas(matriz,linha,aux):
    nome = []
    menor = 0
    x = []
    for i in range(len(matriz)):
        for j in range(len(linha)):
            for k in range(len(aux)):
                if j == 2:
                    if matriz[i][j][k] > menor:
                        menor = matriz[i][j][k]

    for i in range(len(matriz)):
        for j in range(len(linha)):
            for k in range(len(aux)):
                if j == 2:
                    if matriz[i][j][k] < menor:
                        menor = matriz[i][j][k]

    print('\n Times que fizeram menos faltas')
    for i in range(len(matriz)):
        x = matriz[i]
        for j in range(len(x)):
            if x[2][0] == menor:
                nome = x[0].upper()
            elif x[2][1] == menor:
                nome = x[1].upper()
        print(nome)

matriz = []
loop = True
cont = 0
while loop:
    x = input('Deseja adicionar times ? (S/N): ').lower()
    if x == 's':
        cont += 1
        linha = []
        aux = []
        for i in range(2):
            linha.append(input('Digite o nome do time: '))
        for j in range(2):
            if j == 0:
                aux.append(int(input('Digite o numero de faltas do primeiro time: ')))
            else:
                aux.append(int(input('Digite o numero de faltas do segundo time: ')))
        print()
        linha.append(aux)
        matriz.append(linha)
    else:
        if len(matriz) == 0:
            print('O campenato não tem jogos, adicione os times')
            print()
            loop = True
        else:
            loop = False

print('O total de faltas do campeonato é:',faltas(matriz))
print(mais_faltas(matriz,linha,aux))
print(menos_faltas(matriz,linha,aux))