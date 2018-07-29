__author__ = 'Fabio'
def str_entra():
    palavra = input('Digite a palavra para testar: ')
    return palavra.lower().replace(" ", "")

def anagrama(palavra, palavra_2):
    count = 0
    for i in range(len(palavra_2)):
        if palavra.count(palavra_2[i]) == palavra_2.count(palavra_2[i]):
            count += 1
    if count == len(palavra) and len(palavra_2):
        print('São anagramas')
    else:
        print('Não são anagramas')

anagrama(str_entra(), str_entra())
