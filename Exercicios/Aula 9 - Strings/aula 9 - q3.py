__author__ = 'Fabio'
def conta_palavras(frase):
    palavras = 1
    count = 0
    for i in range(len(frase)):
        if frase[i] == ' ':
            count += 1
            if count == 1:
                palavras += 1
        else:
            count = 0
    return palavras
frase = input("Digite uma frase: ")
print('Esta frase tem',conta_palavras(frase),'palavras')