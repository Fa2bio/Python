loop = True
quadrado = 0
while loop is True:
    num = input('Digite o número ou deixe em branco este campo: ')
    if num != '':
        num = int(num)
        quadrado += num**2
    else:
        loop = False
print ('A soma dos quadrados é:',quadrado)