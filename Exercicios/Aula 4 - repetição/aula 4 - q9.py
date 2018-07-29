x = eval(input('Digite o valor de x: '))
y = eval(input('Digite o valor de y: '))
cont = 0

while x >= y:
    x = x-y
    cont += 1
print ('O resto da divisão é:',x)
print ('O número de divisões é:',cont)
