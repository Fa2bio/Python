__author__ = 'Fabio'
b_menor = eval(input('Digite o valor da base menor: '))
b_maior = eval(input('Digite o valor da base maior: '))
alt = eval(input('Digite o valor da altura: '))

if b_menor > 0 and b_maior > 0 and alt > 0:
    area = (b_maior + b_menor * alt) / 2
    print(area)
else:
    print('Digite um número positivo')