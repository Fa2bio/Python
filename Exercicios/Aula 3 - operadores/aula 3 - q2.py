__author__ = 'Fabio'
escol = input('Escolha 1 p/ converter celsius para Farenheit, 2 p/ converter Farenheit para celsius, 3 p/ converter polegada em milimetro e 4 p/ milimetro em polegada: ')

if escol == '1':
    c = eval (input('Digite a temperatura em celsius: '))
    F =(9/5)*c+32
    print(F)

if escol == '2':
    f = eval(input('Digite a temperatura em Farenheit: '))
    c = (5*f - 160)/9
    print(c)

if escol == '3':
    pol = eval(input('Digite a medida em polegadas: '))
    conver = pol * 24.5
    print(conver,'mm')

if escol == '4':
    mm = eval(input('Digite a medida em milimetros: '))
    conver_2 = mm / 24.5
    print(conver_2,'pol')
