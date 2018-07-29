__author__ = 'Fábio'
import math

# Triângulo
def area_circunferência(raio):
    return math.pi*raio**2
def area_triangulo(a, b, c):
    s_perim = (a + b + c) / 2
    return s_perim
def perimetro_triangulo(a, b, c):
    return a+b+c

#Circunferência
def perimetro_circunferência(raio):
    return 2*math.pi*raio

#Retângulo
def area_retangulo(l1,l2):
    return l1*l2
def perimetro_retangulo(l1, l2):
    return 2*(l1 + l2)

cont = True
for i in range(3):
    tipo_figura = eval(input("digite 1 se a figura for uma circunferência, 2 se for um triângulo e 3 se for um retângulo:"))
    if tipo_figura == 1:
        Raio = eval(input("digite o valor do raio:"))
        per_c = perimetro_circunferência(Raio)
        areac = area_circunferência(Raio)
        print("Area = ", areac)
        print("Perímetro = ", per_c)
    if tipo_figura == 2:
        a = eval(input("digite o valor do lado a:"))
        b = eval(input("digite o valor do lado b:"))
        c = eval(input("digite o valor do lado c:"))
        per_t = perimetro_triangulo(a, b, c)
        areat = area_triangulo(a, b, c)
        print("Area = ", areat)
        print("Perímetro = ", per_t)
    if tipo_figura == 3:
        l1 = eval(input("digite o valor do lado 1:"))
        l2 = eval(input("digite o valor do lado 2:"))
        per_r = perimetro_retangulo(l1, l2)
        arear = area_retangulo(l1, l2)
        print("Area = ", arear)
        print("Perímetro = ", per_r)