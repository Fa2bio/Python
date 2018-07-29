def entrada():
    frase = input('Digite uma frase: ')
    return frase

def espaco(frase):
    for i in range(len(frase)):
        if frase[i] == " ":
            frase = frase[:i] + '#' + frase[i+1:]
    return frase

print(espaco(entrada()))