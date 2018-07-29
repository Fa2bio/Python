__author__ = 'Fabio'
def inverso_maiusc(palavra):
    palavra = palavra.upper()
    result = " "
    for inverso in palavra:
        result = inverso + result
    return result

palavra = input('Digite uma palavra: ')
print(inverso_maiusc(palavra))

