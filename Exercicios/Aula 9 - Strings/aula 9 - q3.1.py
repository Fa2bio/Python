def conta_palavras(frase):
    x = frase.split()
    return len(x)

frase = input('Digite uma frase: ')
print('Esta frase tem',conta_palavras(frase),'palavras')