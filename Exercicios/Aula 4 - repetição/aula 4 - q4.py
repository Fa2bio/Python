__author__ = 'Fabio'
loop = True
divisor = 2
cont = 0
while loop is True:
    num = eval(input('Digite um número: '))
    while divisor < num:
        if num % divisor == 0:
            print (divisor)
            cont += 1
        divisor += 1
    if cont == 0:
        print('O número é primo')
    loop = False
    escol = input('Deseja analisar outro número ? (S/N): ')
    if escol == 's' or escol == 'S':
        loop = True
        divisor = 2
        cont = 0