__author__ = 'Fabio'
vet_1 = []
vet_2 = []

vet_1.append(eval(input('Digite o valor de x1: ')))
vet_2.append(eval(input('Digite o valor de x2: ')))
vet_1.append(eval(input('Digite o valor de y1: ')))
vet_2.append(eval(input('Digite o valor de y2: ')))
vet_1.append(eval(input('Digite o valor de z1: ')))
vet_2.append(eval(input('Digite o valor de z2: ')))

result = vet_1[0] + vet_2[0], vet_1[1] + vet_2[1], vet_1[2] + vet_2[2]
print(result)