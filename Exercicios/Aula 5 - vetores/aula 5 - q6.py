__author__ = 'Fabio'
#Leia um vetor de 10 posições e ordene o vetor, usando 3 métodos de ordenação diferentes
#insertion.sort
vet = []
cont = 0
for i in range(10):
    vet.append(eval(input('Digite um valor: ')))

for j in range(len(vet)):
        comparador = vet[j]
        i = j
        while i>0 and vet[i-1]>comparador:
            vet[i] = vet[i-1]
            i -= 1
            cont += 1
        vet[i]=comparador

print(vet)
print(cont)