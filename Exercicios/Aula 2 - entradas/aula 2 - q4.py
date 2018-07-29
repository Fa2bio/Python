__author__ = 'Fabio'
nome = input('Digite o nome do produto: ')
quant = eval(input('Digite a quantidade comprada: '))
valor = eval(input('Digite o valor da unidade: '))
desc = eval(input('Digite o valor do desconto: '))

total = valor * quant - desc*desc/100

print(total)