contador = 1

while True:
    p, r = map(int, input().split(" "))
    if p == 0 and r == 0:
        break

    fila = []
    entrada = input().split()
    print(p,r)
    for i in range(p):
        fila.append(int(entrada[i]))

    for i in range(r):
        entrada = input().split(" ")

        #participantes = int(entrada[0])
        ordem = int(entrada[1])

        k = 2
        for j in range(len(fila)):
            if fila[j] == 0:
                continue
            else:
                if ordem != int(entrada[k]):
                    fila[j] = 0
                k += 1

    print("Teste " + str(contador))
    for i in fila:
        if i != 0:
            print(i)
    print("")

    contador += 1