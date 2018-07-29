__author__ = 'Fabio'
esco = input('O que deseja operar ? Soma, subtração, multiplicação ou divisão ?: ')
num1 = eval(input('Digite um número: '))
num2 = eval(input('Digite um número: '))

if esco == 'soma':
    soma = num1 + num2
    print(soma)
if esco == 'subtração':
    sub = num1 - num2
    print(sub)
if esco == 'multiplicação':
    mult = num1 * num2
    print(mult)
if esco == 'divisão':
    div = num1 / num2
    print(div)