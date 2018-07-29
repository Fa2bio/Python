__author__ = 'Fabio'
import math
lado_ret = eval(input('Digite o lado: '))
alt_ret = eval(input('Digite a base: '))
area_ret = lado_ret*alt_ret

r = 2
area_cir = math.pi*r**2

area_n = area_ret - area_cir

print(area_n)