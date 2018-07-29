matriz = []
nome = []
aux = []
aux_2 = []
menor_cons = 0

n = eval(input('Quantos carros você deseja adicionar ?: '))

for i in range(n):
    linha = []
    for j in range(2):
        if j == 0:
            linha.append(input('Digite o nome do carro: '))
        else:
            x = eval(input('Qual o consumo do carro ? (KM/L): '))
            linha.append(x)
            if i < n and j != 0:
                car = (1000 / x)
                car_1 = car * 3.5
                aux.append(car)
                aux_2.append(car_1)
    matriz.append(linha)

for i in range(len(matriz)):
    for j in range(len(matriz)):
        if j != 0:
            if matriz[i][1] > menor_cons:
                menor_cons = matriz[i][1]

aux_1 = matriz[:]
menor = []

print('\nModelo(s) mais economico(s):')
for i in range(len(aux_1)):
    for j in range(len(aux_1)):
        if j != 0:
            if aux_1[i][1] == menor_cons:
                if aux_1[i][0] != menor:
                    print(aux_1[i][0])
                    menor = aux_1[i][0]
print()
for i in range(n):
    for j in range(len(aux)):
        if i == j:
            print('O carro',matriz[i][0],'consumiu',round(aux[j],2),'litros','e foram gastos R$',round(aux_2[j],2))
