__author__ = 'Fabio'
x = (eval(input('Digite um número para comparação: ')))
vet = []
pos = -1

for i in range(5):
    vet.append(eval(input('Digite um número: ')))

for i in range(len(vet)):
    if vet[i] == x:
        pos = i
print(pos)