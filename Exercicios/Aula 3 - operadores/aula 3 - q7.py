__author__ = 'Fabio'
x = eval(input('Digite o valor da coordenada x do ponto: '))
y = eval(input('Digite o valor da coordenada y do ponto: '))

if x < 0 and y > 0:
    print('As coordenadas do ponto é(',x,',',y,')','e o número esta no primeiro quadrante.')
if x > 0 and y >0:
    print('As coordenadas do ponto é(',x,',',y,')','e o numero esta no segundo quadrante.')
if x < 0 and y <0:
    print('As coordenadas do ponto é(',x,',',y,')','e o numero esta no terceiro quadrante.')
if x > 0 and y <0:
    print('As coordenadas do ponto é(',x,',',y,')','e o numero esta no quarto quadrante.')
if x == 0 and y ==0:
    print('As coordenadas do ponto é(',x,',',y,')','e o número esta sobre a origem, portanto o valor é 0.')
if x == 0 and (y <0 or y >0):
    print('As coordenadas do ponto é(',x,',',y,')','-1')
if y == 0 and (x < 0 or x > 0):
    print('As coordenadas do ponto é(',x,',',y,')','-1')
