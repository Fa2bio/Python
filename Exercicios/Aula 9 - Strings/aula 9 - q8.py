__author__ = 'Fabio'
def str_original():
    palavra = input("Digite seu nome: ")
    return palavra

def manipulacao(a):
    for i in range(len(a)):
        print(a[:i+1].upper())


manipulacao(str_original())
