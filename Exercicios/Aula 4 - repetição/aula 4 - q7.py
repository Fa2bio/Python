__author__ = 'Fabio'
num = eval(input('Digite o número: '))
triangular = 0
for i in range(num):
    if i%2 == 0:
        if i * (i + 1) * (i + 2) == num:
            triangular = i * (i+1) * (i+2)

if triangular == num:
    print('O número é triangular')
else:
    print('O número não é triangular')
