__author__ = 'Fabio'
vet = []
aux = []
for i in range(5):
    vet.append(eval(input('Digite um número :')))

for i in range(len(vet)):
    if i == 0:
        aux.append(vet[i])
    else:
        for j in range(len(aux)-1,len(vet)-1,-1):
            if vet[i] != aux[j]:
                aux.append(vet[i])
print(len(aux))