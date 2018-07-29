__author__ = 'Fabio'
from random import randint
vet = []
cont = 0
soma = 0
pos = 0
maior = 0

for i in range(50):
    vet.append(randint(0,20))
print (vet)

#soma os elementos do vetor
for j in range(len(vet)):
    soma = soma + vet[j]
print('A soma dos elementos é: ',soma)

#verifica quantas vezes o 9 apareceu
for k in range(len(vet)):
    if vet[k] == 9:
        cont += 1
print('O número de vezes em que o 9 apareceu foi: ',cont)

#acha o maior valor do vetor
for l in range(len(vet)):
    if vet[l] > maior:
        maior = vet[l]
print ('O maior número é:',maior)

#acha a posição do maior número
for m in range(len(vet)-1,-1,-1):
    if vet[m] == maior:
        pos = m
        print('A posição do maior número é:',pos)


