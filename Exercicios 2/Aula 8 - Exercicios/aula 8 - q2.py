def invertido(vetor):
    aux = vetor[:]
    for j in range(len(aux) // 2):
        auxiliar = aux[j]
        aux[j] = aux[len(aux) - j - 1]
        aux[len(aux) - j - 1] = auxiliar
    return aux

vetor = []
loop = True
while loop is True:
    string = input('Digite algo ou deixe este campo em branco: ')
    if string != '':
        vetor.append(string)
    else:
        loop = False

print('Vetor original:',vetor)
print('Vetor invertido:',invertido(vetor))