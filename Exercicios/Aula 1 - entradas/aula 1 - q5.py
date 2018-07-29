__author__ = 'Fabio'
num_centavos = float (input ('Digite o número de centavos: '))
num_centavos = num_centavos*100
num_moedas = 0

num_moedas = num_centavos //100
print (num_moedas, 'moedas de 1 real')
num_centavos = num_centavos - (num_moedas*100)

num_moedas = num_centavos //50
print (num_moedas, 'moedas de 50 centavos')
num_centavos = num_centavos - (num_moedas*50)

num_moedas = num_centavos //25
print (num_moedas, 'moedas de 25 centavos')
num_centavos = num_centavos - (num_moedas*25)

num_moedas = num_centavos //10
print (num_moedas, 'moedas de 10 centavos')
num_centavos = num_centavos - (num_moedas*10)

num_moedas = num_centavos //5
print (num_moedas, 'moedas de 5 centavos')
num_centavos = num_centavos - (num_moedas*5)

num_moedas = num_centavos //1
print (num_moedas, 'moedas de 1 centavos')
num_centavos = num_centavos - (num_moedas*1)