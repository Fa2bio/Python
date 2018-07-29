__author__ = 'Fabio'
from random import randint

vet_dados = []
vet_cont = []
for i in range(10):
    vet_dados.append(randint(1,6))

for i in range(len(vet_dados)):
    if i > 0 and i < 7:
        vet_cont.append(vet_dados.count(i))

print('O vetor gerado é:',vet_dados)
print('A quantidade de cada valor é:',vet_cont)