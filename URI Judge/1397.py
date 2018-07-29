while True:
    r = int(input())
    if r == 0:
        break

    soma_um = 0
    soma_dois = 0
    jogos = []
    for i in range(r):
        aux = []
        jog_um, jog_dois = map(int, input().split(" "))
        aux.append(jog_um)
        aux.append(jog_dois)
        jogos.append(aux)

    for i in range(len(jogos)):
        for j in range(len(jogos[i])):
            if j < 1:
                if jogos[i][j] > jogos[i][j+1]:
                    soma_um += 1
                elif jogos[i][j] == jogos[i][j+1]:
                    soma_um += 0
                    soma_dois += 0
                else:
                    soma_dois += 1
            else:
                pass

    print(soma_um,soma_dois)

