__author__ = 'Fabio'
from random import randint
n = eval(input('Digite o valor N para finalizar o sorteio do número: '))
vet_original = []

for i in range(5):
    num = (randint(0,n))
    vet_original.append(num)

print('Vetor original:',vet_original)

for j in range(len(vet_original)//2):
    auxiliar = vet_original[j]
    vet_original[j] = vet_original[len(vet_original)-j-1]
    vet_original[len(vet_original) - j-1] = auxiliar

print('Vetor manipulado:',vet_original)