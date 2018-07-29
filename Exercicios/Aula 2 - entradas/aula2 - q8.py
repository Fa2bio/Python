__author__ = 'Fabio'
h = eval(input('Digite o valor em horas: '))
min = eval(input('Digite o valor em minutos: '))
seg = eval(input('Digite o valor em segundos: '))
h1 = h*3600
min2 = min*60

total = h1 + min2 + seg

print(total, 'segundos')