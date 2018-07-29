__author__ = 'Fabio'
def muda_frase (frase,antiga,nova):
    frase = frase.replace(antiga,nova)
    pos = frase.count(nova)-1
    frase = frase.replace(nova,antiga,pos)
    return frase

frase = input('Digite uma frase: ')
antiga = input('Digite a palavra antiga: ')
nova = input('Digite a palavra nova: ')

print(muda_frase(frase,antiga,nova))