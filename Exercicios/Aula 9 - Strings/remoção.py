vet = [1,3,9,1,4]
vet_b = [69,36,5]
vet_c = []

vet += vet_b
g = 0
pos = 0
tam = len(vet)
while g < tam:
    menor = 0
    for i in range(len(vet)):
        if vet[i] > menor:
            menor = vet[i]

    for k in range(len(vet)):
        if vet[k] < menor and vet != 0:
            menor = vet[k]
            pos = k
    vet_c.append(menor)
    vet.remove(menor)

    g += 1

print(vet_c)