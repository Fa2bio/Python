__author__ = 'Fabio'
cli_1 = eval(input('Digite o número de cadastro do cliente: '))
cli_2 = eval(input('Digite o número de cadastro do cliente: '))
cli_3 = eval(input('Digite o número de cadastro do cliente: '))

val_1 = eval(input('Digite o valor gasto do cliente: '))
val_2 = eval(input('Digite o valor gasto do cliente: '))
val_3 = eval(input('Digite o valor gasto do cliente: '))

total = val_1 + val_2 + val_3
media = (val_1 + val_2 + val_3)/3
cont = 0

if val_1 > 100:
    print('O código de cliente é:',cli_1)
if val_2 > 100:
    print('O código de cliente é:',cli_2)
if val_3 > 100:
    print('O código de cliente é:',cli_3)

if val_1 < 50:
    cont = cont +1
if val_2 < 50:
    cont = cont +1
if val_3 < 50:
    cont = cont +1

print('O total gasto foi de', total, 'a media foi', media, 'e o número de clientes que fizeram compras abaixo de 50 reais foi:', cont)

