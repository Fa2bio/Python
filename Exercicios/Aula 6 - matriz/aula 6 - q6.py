matriz = []

#piloto com a melhor volta e a volta
melhor_volta = [] #volta com o tempo mais baixo
coluna_menor = []  #posição da volta com o menor tempo
melhor_piloto = []

#classificação
classifi = []

#media de cada volta
vol_1 = 0
vol_2 = 0
vol_3 = 0
vol_4 = 0
vol_5 = 0
vol_6 = 0
vol_7 = 0
vol_8 = 0
vol_9 = 0
vol_10 = 0

cont_1 = 0
cont_2 = 0
cont_3 = 0
cont_4 = 0
cont_5 = 0
cont_6 = 0
cont_7 = 0
cont_8 = 0
cont_9 = 0
cont_10 = 0


#preenche a matriz
for i in range(3):
    linha =[]
    pilotos = []
    soma = 0
    for j in range(3):
        if j == 0:
            nome = input('Digite o nome do corredor: ')
            linha.append(nome)
            pilotos.append(nome)
        else:
            num = eval(input('Digite o tempo da volta['+ str(j) + ']: '))
            linha.append(num)
            # acha a volta mais lenta
            if len(melhor_volta) == 0:
                melhor_volta.append(num)
            else:
                for i in range(len(melhor_volta)):
                    if num != 0 and num > melhor_volta[i]:
                        melhor_volta[0] = num

            #gera a soma das voltas de cada piloto
            #if i == 0 and j != 0:
            #   soma += num
            #    if j == 10:
            #        pilotos.append(soma)
            #        pilotos = pilotos[::-1]
            #elif i == 1 and j != 0:
            #    soma += num
            #    if j == 10:
            #        pilotos.append(soma)
            #        pilotos = pilotos[::-1]
            #elif i == 2 and j != 0:
            #   soma += num
            #    if j == 10:
            #        pilotos.append(soma)
            #        pilotos = pilotos[::-1]
            #elif i == 3 and j != 0:
            #    soma += num
            #    if j == 10:
            #        pilotos.append(soma)
            #        pilotos = pilotos[::-1]
            #elif i == 4 and j != 0:
            #    soma += num
            #    if j == 10:
            #        pilotos.append(soma)
            #        pilotos = pilotos[::-1]
            #elif i == 5 and j != 0:
            #    soma += num
            #    if j == 10:
            #        pilotos.append(soma)
            #        pilotos = pilotos[::-1]

            #acha a media de cada volta
            if j == 1 and num != 0:
                vol_1 += num
                cont_1 += 1
            elif j == 2 and num != 0:
                vol_2 += num
                cont_2 += 1
            elif j == 3 and num != 0:
                vol_3 += num
                cont_3 += 1
            elif j == 4 and num != 0:
                vol_4 += num
                cont_4 += 1
            elif j == 5 and num != 0:
                vol_5 += num
                cont_5 += 1
            elif j == 6 and num != 0:
                vol_6 += num
                cont_6 += 1
            elif j == 7 and num != 0:
                vol_7 += num
                cont_7 += 1
            elif j == 8 and num != 0:
                vol_8 += num
                cont_8 += 1
            elif j == 9 and num != 0:
                vol_9 += num
                cont_9 += 1
            elif j == 10 and num != 0:
                vol_10 += num
                cont_10 += 1
    classifi.append(pilotos)
    matriz.append(linha)

#acha a volta com o menor tempo
for i in range(3):
    for j in range(3):
        if j != 0:
            #acha a volta mais rápida
            for l in range(len(melhor_volta)):
                if matriz[i][j] != 0 and matriz[i][j] < melhor_volta[0]:
                    melhor_volta[0] = matriz[i][j]
        if j != 0:
            coluna_menor.append(j)
            melhor_piloto.append(matriz[i][0])
    if j != 0:
        coluna_menor[0] = j
        melhor_piloto[0] = matriz[i][0]

#acha os iguais da melhor volta
for i in range(3):
    for j in range(3):
        if j != 0:
            for k in range(len(melhor_volta)):
                if matriz[i][j] != 0 and matriz[i][j] == melhor_volta[k]:
                    melhor_volta.append(matriz[i][j])
                    coluna_menor.append(j)
                    melhor_piloto.append(matriz[i][0])

print()
print('O melhor tempo foi:',melhor_volta)
print('O piloto com a melhor volta foi o(a):',melhor_piloto,'na volta',coluna_menor)

#ordena a classificação


for i in range(len(classifi)):
    if i == 0:
        classifi.sort()
#gera a classificação dos pilotos
for i in range(1):
    print ('A classificação é:')
    pos = 1
    for j in range(6):
        print('Em',pos,'lugar:',classifi[j][1])
        pos += 1

#acha a volta com a media mais rápida
vol_1 /= cont_1
vol_2 /= cont_2
vol_3 /= cont_3
vol_4 /= cont_4
vol_5 /= cont_5
vol_6 /= cont_6
vol_7 /= cont_7
vol_8 /= cont_8
vol_9 /= cont_9
vol_10 /= cont_10

if (vol_1 <= vol_2) and (vol_1 <= vol_3) and (vol_1 <= vol_4) and (vol_1 <= vol_5) and (vol_1 <= vol_6) and (vol_1 <= vol_7) and (vol_1 <= vol_8) and (vol_1 <= vol_9) and (vol_1 <= vol_10):

    if vol_1 == vol_2 and (vol_1 < vol_3) and (vol_1 < vol_4) and (vol_1 < vol_5) and (vol_1 < vol_6) and (vol_1 < vol_7) and (vol_1 < vol_8) and (vol_1 < vol_9) and (vol_1 < vol_10):
        print('A volta 1 e a volta 2 foram as voltas com as médias mais rápidas')

    elif vol_1 == vol_3 and vol_1 < vol_2 and (vol_1 < vol_4) and (vol_1 < vol_5) and (vol_1 < vol_6) and (vol_1 < vol_7) and (vol_1 < vol_8) and (vol_1 < vol_9) and (vol_1 < vol_10):
        print('A volta 1 e a volta 3 foram as voltas com as médias mais rápidas')

    elif vol_1 == vol_4 and vol_1 < vol_3 and vol_1 < vol_2 and (vol_1 < vol_5) and (vol_1 < vol_6) and (vol_1 < vol_7) and (vol_1 < vol_8) and (vol_1 < vol_9) and (vol_1 < vol_10):
        print('A volta 1 e a volta 4 foram as voltas com as médias mais rápidas')

    elif vol_1 == vol_5 and vol_1 < vol_4 and vol_1 < vol_3 and vol_1 < vol_2 and (vol_1 < vol_6) and (vol_1 < vol_7) and (vol_1 < vol_8) and (vol_1 < vol_9) and (vol_1 < vol_10):
        print('A volta 1 e a volta 5 foram as voltas com as médias mais rápidas')

    elif vol_1 == vol_6 and vol_1 < vol_5 and vol_1 < vol_4 and vol_1 < vol_3 and vol_1 < vol_2 and (vol_1 < vol_7) and (vol_1 < vol_8) and (vol_1 < vol_9) and (vol_1 < vol_10):
        print('A volta 1 e a volta 6 foram as voltas com as médias mais rápidas')

    elif vol_1 == vol_7 and vol_1 < vol_6 and vol_1 < vol_5 and vol_1 < vol_4 and vol_1 < vol_3 and vol_1 < vol_2 and (vol_1 < vol_8) and (vol_1 < vol_9) and (vol_1 < vol_10):
        print('A volta 1 e a volta 7 foram as voltas com as médias mais rápidas')

    elif vol_1 == vol_8 and vol_1 < vol_7 and vol_1 < vol_6 and vol_1 < vol_5 and vol_1 < vol_4 and vol_1 < vol_3 and vol_1 < vol_2 and (vol_1 < vol_9) and (vol_1 < vol_10):
        print('A volta 1 e a volta 8 foram as voltas com as médias mais rápidas')

    elif vol_1 == vol_9 and vol_1 < vol_8 and vol_1 < vol_7 and vol_1 < vol_6 and vol_1 < vol_5 and vol_1 < vol_4 and vol_1 < vol_3 and vol_1 < vol_2 and (vol_1 < vol_10):
        print('A volta 1 e a volta 9 foram as voltas com as médias mais rápidas')

    elif vol_1 == vol_10 and vol_1 < vol_9 and vol_1 < vol_8 and vol_1 < vol_7 and vol_1 < vol_6 and vol_1 < vol_5 and vol_1 < vol_4 and vol_1 < vol_3 and vol_1 < vol_2:
        print('A volta 1 e a volta 10 foram as voltas com as médias mais rápidas')

    else:
        print('A volta com a média mais rápida foi a 1')

elif (vol_2 <= vol_1) and (vol_2 <= vol_3) and (vol_2 <= vol_4) and (vol_2 <= vol_5) and (vol_2 <= vol_6) and (vol_2 <= vol_7) and (vol_2 <= vol_8) and (vol_2 <= vol_9) and (vol_2 <= vol_10):
    if vol_2 == vol_3:
        print('A volta 2 e a volta 3 foram as voltas com as médias mais rápidas')
    elif vol_2 == vol_4:
        print('A volta 2 e a volta 4 foram as voltas com as médias mais rápidas')
    elif vol_2 == vol_5:
        print('A volta 2 e a volta 5 foram as voltas com as médias mais rápidas')
    elif vol_2 == vol_6:
        print('A volta 2 e a volta 6 foram as voltas com as médias mais rápidas')
    elif vol_2 == vol_7:
        print('A volta 2 e a volta 7 foram as voltas com as médias mais rápidas')
    elif vol_2 == vol_8:
        print('A volta 2 e a volta 8 foram as voltas com as médias mais rápidas')
    elif vol_2 == vol_9:
        print('A volta 2 e a volta 9 foram as voltas com as médias mais rápidas')
    elif vol_2 == vol_10:
        print('A volta 2 e a volta 10 foram as voltas com as médias mais rápidas')
    else:
        print('A volta com a média mais rápida foi a 2')

elif (vol_3 <= vol_1) and (vol_3 <= vol_2) and (vol_3 <= vol_4) and (vol_3 <= vol_5) and (vol_3 <= vol_6) and (vol_3 <= vol_7) and (vol_3 <= vol_8) and (vol_3 <= vol_9) and (vol_3 <= vol_10):
    if vol_3 == vol_4:
        print('A volta 3 e a volta 4 foram as voltas com as médias mais rápidas')
    elif vol_3 == vol_5:
        print('A volta 3 e a volta 5 foram as voltas com as médias mais rápidas')
    elif vol_3 == vol_6:
        print('A volta 3 e a volta 6 foram as voltas com as médias mais rápidas')
    elif vol_3 == vol_7:
        print('A volta 3 e a volta 7 foram as voltas com as médias mais rápidas')
    elif vol_3 == vol_8:
        print('A volta 3 e a volta 8 foram as voltas com as médias mais rápidas')
    elif vol_3 == vol_9:
        print('A volta 3 e a volta 9 foram as voltas com as médias mais rápidas')
    elif vol_3 == vol_10:
        print('A volta 3 e a volta 10 foram as voltas com as médias mais rápidas')
    else:
        print('A volta com a média mais rápida foi a 3')

elif (vol_4 <= vol_1) and (vol_4 <= vol_2) and (vol_4 <= vol_3) and (vol_4 <= vol_5) and (vol_4 <= vol_6) and (vol_4 <= vol_7) and (vol_4 <= vol_8) and (vol_4 <= vol_9) and (vol_4 <= vol_10):
    if vol_4 == vol_5:
        print('A volta 4 e a volta 5 foram as voltas com as médias mais rápidas')
    elif vol_4 == vol_6:
        print('A volta 4 e a volta 6 foram as voltas com as médias mais rápidas')
    elif vol_4 == vol_7:
        print('A volta 4 e a volta 7 foram as voltas com as médias mais rápidas')
    elif vol_4 == vol_8:
        print('A volta 4 e a volta 8 foram as voltas com as médias mais rápidas')
    elif vol_4 == vol_9:
        print('A volta 4 e a volta 9 foram as voltas com as médias mais rápidas')
    elif vol_4 == vol_10:
        print('A volta 4 e a volta 10 foram as voltas com as médias mais rápidas')
    else:
        print('A volta com a média mais rápida foi a 4')

elif (vol_5 <= vol_1) and (vol_5 <= vol_2) and (vol_5 <= vol_3) and (vol_5 <= vol_4) and (vol_5 <= vol_6) and (vol_5 <= vol_7) and (vol_5 <= vol_8) and (vol_5 <= vol_9) and (vol_5 <= vol_10):
    if vol_5 == vol_6:
        print('A volta 5 e a volta 6 foram as voltas com as médias mais rápidas')
    elif vol_5 == vol_7:
        print('A volta 5 e a volta 7 foram as voltas com as médias mais rápidas')
    elif vol_5 == vol_8:
        print('A volta 5 e a volta 8 foram as voltas com as médias mais rápidas')
    elif vol_5 == vol_9:
        print('A volta 5 e a volta 9 foram as voltas com as médias mais rápidas')
    elif vol_5 == vol_10:
        print('A volta 5 e a volta 10 foram as voltas com as médias mais rápidas')
    else:
        print('A volta com a média mais rápida foi a 5')

elif (vol_6 <= vol_1) and (vol_6 <= vol_2) and (vol_6 <= vol_3) and (vol_6 <= vol_4) and (vol_6 <= vol_5) and (vol_6 <= vol_7) and (vol_6 <= vol_8) and (vol_6 <= vol_9) and (vol_6 <= vol_10):
    if vol_6 == vol_7:
        print('A volta 6 e a volta 7 foram as voltas com as médias mais rápidas')
    elif vol_6 == vol_8:
        print('A volta 6 e a volta 8 foram as voltas com as médias mais rápidas')
    elif vol_6 == vol_9:
        print('A volta 6 e a volta 9 foram as voltas com as médias mais rápidas')
    elif vol_6 == vol_10:
        print('A volta 6 e a volta 10 foram as voltas com as médias mais rápidas')
    else:
        print('A volta com a média mais rápida foi a 6')

elif (vol_7 <= vol_1) and (vol_7 <= vol_2) and (vol_7 <= vol_3) and (vol_7 <= vol_4) and (vol_7 <= vol_5) and (vol_7 <= vol_6) and (vol_7 <= vol_8) and (vol_7 <= vol_9) and (vol_7 <= vol_10):
    if vol_7 == vol_8:
        print('A volta 7 e a volta 8 foram as voltas com as médias mais rápidas')
    elif vol_7 == vol_9:
        print('A volta 7 e a volta 9 foram as voltas com as médias mais rápidas')
    elif vol_7 == vol_10:
        print('A volta 7 e a volta 10 foram as voltas com as médias mais rápidas')
    else:
        print('A volta  com a média mais rápida foi a 6')

elif (vol_8 <= vol_1) and (vol_8 <= vol_2) and (vol_8 <= vol_3) and (vol_8 <= vol_4) and (vol_8 <= vol_5) and (vol_8 <= vol_6) and (vol_8 <= vol_7) and (vol_8 <= vol_9) and (vol_8 <= vol_10):
    if vol_8 == vol_9:
        print('A volta 8 e a volta 9 foram as voltas com as médias mais rápidas')
    elif vol_8 == vol_10:
        print('A volta 8 e a volta 10 foram as voltas com as médias mais rápidas')
    else:
        print('A volta com a média mais rápida foi a 8')
elif (vol_9 <= vol_1) and (vol_9 <= vol_2) and (vol_9 <= vol_3) and (vol_9 <= vol_4) and (vol_9 <= vol_5) and (vol_9 <= vol_6) and (vol_9 <= vol_7) and (vol_9 <= vol_8) and (vol_9 <= vol_10):
    if vol_9 == vol_10:
        print('A volta 9 e a volta 10 foram as voltas com as médias mais rápidas')
    else:
        print('A volta com a média mais rápida foi a 9')

elif (vol_1 == vol_2) and (vol_1 == vol_3) and (vol_1 == vol_4) and (vol_1 == vol_5) and (vol_1 == vol_6) and (vol_1 == vol_7) and (vol_1 == vol_8) and (vol_1 == vol_9) and (vol_1 == vol_10):
    print('As médias das voltas são iguais')

else:
    print('A volta com a média mais rápida foi a 10')