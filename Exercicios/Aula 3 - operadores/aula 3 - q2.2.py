import math
l1x = eval(input('Digite a coordenada x1: '))
l2x = eval(input('Digite a coordenada x2: '))
l3x = eval(input('Digite a coordenada x3: '))

l1y = eval(input('Digite a coordenada y1: '))
l2y = eval(input('Digite a coordenada y2: '))
l3y = eval(input('Digite a coordenada y3: '))

determ = (l1x*l2y+l3x*l1y+l2x*l3y-l3x*l2y-l1x*l3y-l2x*l1y)/2
if determ == 0:
    print ('Não é triangulo')
else:
    dist1 = math.sqrt((l2x-l1x)**2 + (l2y -l1y)**2)
    dist2 = math.sqrt((l3x-l2x)**2 + (l3y - l2y)**2)
    dist3 = math.sqrt((l1x-l3x)**2 + (l1y - l3y)**2)

    if (dist1==dist2 and dist1==dist3):
        print('O triangulo é equilatero')
    if (dist1==dist2 and dist1!=dist3):
        print('O triangulo é isósceles')
    if (dist1!=dist2 and dist1!=dist3):
        print('O triangulo é escaleno')