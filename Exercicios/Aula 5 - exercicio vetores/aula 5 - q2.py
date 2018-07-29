__author__ = 'Fabio'
from random import randint
vet = []

for i in range(10):
    vet.append(randint(0,20))
print('Vetor original', vet)

for i in range(len(vet)):
    difere = vet[i-1]
    if vet[i] != difere[i+1]:
