test = 0

while True:
    rep = int(input())
    if rep != 0:
        test += 1
        print("Teste ", test)
        saldo = []
        for i in range(rep):
            rodada_um, rodada_dois = map(int, input().split())
            saldo.append(rodada_um - rodada_dois)

        pos_inicial = 0
        pos_final = 0
        nenhum = True
        for j in range(len(saldo)):
            if saldo[j] > 0:
                nenhum = False
                for k in range(len(saldo)-1,-1,-1):
                    if saldo[k] > 0:
                        for l in range(j,k,1):
                            if saldo[j] > saldo[l]and saldo[j]!= saldo[l] and saldo[k]!=saldo[l]:
                                pos_inicial = j +1
                                pos_final = k + 1
        if nenhum:
            print("nenhum")
        else:
            print(pos_inicial,pos_final)
    else:
        break