__author__ = 'Fabio'
from random import randint
vet = []
cont = 0

for i in range(50):
    vet.append(randint(1,6))

for i in range(len(vet)):
    if vet[i] == 6:
        cont += 1

cal = (cont / 50)*100

print('O número saiu',cont,'vezes','e isso da um total de',cal,'%')