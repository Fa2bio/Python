__author__ = 'Fabio'
loop = True
vet = []
cont_cinco = 0
soma_par = 0
soma_impar = 0
cont_num = 0

while loop is True:
    num = int(eval(input('Digite um número: ')))
    if num >= 0:
        vet.append(num)
        cont_num += 1
    else:
        loop = False

for i in range(len(vet)):
    if vet[i]>5:
        cont_cinco += 1
    if vet[i]%2 == 0:
        soma_par += vet[i]
    if vet[i]%2 != 0:
        soma_impar += vet[i]

print (vet)
print ('A quantidade de valores maiores que cinco é:',cont_cinco)
print ('A soma dos números pares é:',soma_par)
print ('A soma dos números ímpares é:',soma_impar)
print('A quantidade de valores inseridos é:',cont_num)