alt = eval(input('Digite a altura: '))
peso = eval(input('Digite o peso: '))
imc = peso/alt**2

if (imc < 18.5):
    print('Abaixo do peso')
if (imc >= 18.6 and imc <= 24.9):
    print('Saudavel')
if (imc >= 25.0 and imc <=29.9):
    print('Peso em excesso')
if (imc >= 30.0 and imc <=34.9):
    print('Obesidade grau I')
if (imc >= 35.0 and imc <= 39.9):
    print('Obesidade grau II (severa)')
if (imc >= 40.0):
    print('Obesidade grau III(mórbida)')
