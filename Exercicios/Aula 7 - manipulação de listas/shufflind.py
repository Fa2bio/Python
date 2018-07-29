from random import randint
def embaralha(list):
    i = len(list)
    while i > 0:
        i -= 1
        j = randint(0,i)  # 0 <= j <= i-1
        aux = list[i]
        list[i] = list[j]
        list[j] = aux
    return list

def orndena(list):
    aux = list[:]
    list = []
    tam = len(aux)
    for i in range(tam):
        menor = aux[0]
        for j in range(len(aux)):
            if aux[j] < menor:
                menor = aux[j]
        list.append(menor)
        aux.remove(menor)
    return list

list = []
loop = True
while loop:
    x = input('Digite um número ou deixe em branco: ')
    if x != '':
        x = eval(x)
        list.append(x)
    else:
        loop = False

for i in range(20):
    if i == 0:
        print('Lista original: ', list)
        print()
        print('Lista orndenada: ',orndena(list))
        print('Lista manipulada: ',embaralha(orndena(list)))
        print()
    else:
        print('Lista orndenada: ',orndena(list))
        print('Lista manipulada: ',embaralha(orndena(list)))
        print()