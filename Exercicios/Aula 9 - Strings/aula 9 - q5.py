__author__ = 'Fabio'
def str_entr():
    palavra = input('Digite uma palavra para verificação: ')
    return palavra


def str_veri(palavra_1, palavra_2):
        compara = palavra_2[::-1]
        if palavra_1 == compara:
            return 'São palindromos'
        else:
            return 'Não são palindromos'

print(str_veri(str_entr(), str_entr()))