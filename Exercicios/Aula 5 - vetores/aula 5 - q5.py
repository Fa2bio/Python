__author__ = 'Fabio'
vet = []
pos = []
semdup = []
aux = 0
aux_2 = 0

for i in range(20):
    vet.append(eval(input('Digite um número: ')))

for j in range(len(vet)):
    if vet[j]>=0 and vet[j] == int(vet[j]):
        pos.append(vet[j])

fora_rep = list(set(pos))
for k in range(len(fora_rep)):
    semdup.append(fora_rep[k])

print(vet)
print(pos)
print(semdup)