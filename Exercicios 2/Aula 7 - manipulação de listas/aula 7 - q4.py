lista_1 = []
lista_2 = []
lista_inter = []
aux = []

n = eval(input('Quantos números você deseja na lista 1? '))
for i in range(n):
    lista_1.append(eval(input('Digite um número: ')))

m = eval(input('Quantos números você deseja na lista 2? '))
for j in range(m):
    lista_2.append(eval(input('Digite um número: ')))

for i in range(len(lista_1)):
    for j in range(len(lista_2)):
        if i == j:
            lista_inter.append(lista_1[i])
            lista_inter.append(lista_2[j])

if len(lista_1) > len(lista_2):
    for i in range(len(lista_1)):
        if i == len(lista_1)-1:
            for j in range(len(lista_1)-1, len(lista_2)-1, -1):
                aux.append(lista_1[j])
    lista_inter += aux[::-1]
else:
    for i in range(len(lista_2)):
        if i == len(lista_2)-1:
            for j in range(len(lista_2)-1, len(lista_1)-1, -1):
                aux.append(lista_2[j])
    lista_inter += aux[::-1]

print()
print('Lista 1 =',lista_1)
print('Lista 2 =',lista_2)
print('Lista intercalada =',lista_inter)