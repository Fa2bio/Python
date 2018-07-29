__author__ = 'Fabio'
#Leia um vetor de 10 posições e ordene o vetor, usando 3 métodos de ordenação diferentes
#bubble.sort
vet = []

cont = 0
for i in range(10):
    vet.append(eval(input('Digite um valor: ')))

for j in range(0,len(vet)-1):
    for k in range(0,len(vet)-1):
        if vet[k]>vet[k+1]:
            aux = vet[k]
            vet[k] = vet [k+1]
            vet[k+1] = aux
        cont += 1
print(vet)
print(cont)
