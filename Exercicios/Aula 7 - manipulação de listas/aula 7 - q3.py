loop = True
notas = []
cont = 0
media = 0
prox_media = 0

while loop is True:
    x = input('Digite um número positivo para nota ou deixe este campo em branco: ')
    if x != '':
        x = eval(x)
        if x >= 0:
            notas.append(x)
            cont += 1
            media += x
    else:
        loop = False
        media /= cont

if cont == 1:
    print('A nota mais próxima é a propria média:',media)
else:
    media = round(media, 2)
    print('As notas dos alunos são:', notas)
    print('Média =', media)
    notas.append(media)
    notas.sort()

    for i in range(len(notas)):
        if notas[i] == media and cont > 2:
            if (media - notas[i-1]) < (notas[i+1] - media):
                prox_media = notas[i-1]
                print('A nota mais próxima esta abaixo da média e é:', prox_media)
            elif (media - notas[i-1]) > (notas[i+1] - media):
                prox_media = notas[i+1]
                print('A nota mais próxima esta acima da média e é:', prox_media)

        elif notas[i] == media and cont == 2:
            prox_media = notas[i - 1]
            print('A nota mais próxima esta abaixo da média e é:', prox_media)