import math

while True:
    hora_inicial, min_inicial, hora_fim, min_fim = map(int, input().split(" "))
    if (hora_inicial == 0) and (min_inicial == 0) and (hora_fim == 0) and (min_fim == 0):
        break

    hora_prox = (hora_inicial*60) + min_inicial
    sono = (hora_inicial+1)*60 - hora_prox
    min = 0
    hora_prox = hora_inicial+1
    dia = 0
    if hora_inicial > hora_fim:
        dia = 1

    while hora_prox < 24:
        if min == 59:
            sono += 60
            min = 0
            hora_prox += 1
        else:
            min += 1
    print(sono)

    if hora_fim > 0:
        hora_prox = ((hora_fim * 60) + min_fim) - (hora_fim-1)*60
        sono += hora_prox
        min = 0
        hora_prox = hora_fim - 1

        while hora_prox > 0:
            if min == 59:
                sono += 60
                min = 0
                hora_prox -= 1
            else:
                min += 1
    else:
        sono += min_fim

    print(sono)