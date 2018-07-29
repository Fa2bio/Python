test = 0

while True:
    r = int(input())
    test += 1
    if r == 0:
        break

    aldo = 0
    beto = 0
    for i in range(r):
        jog_um, jog_dois = map(int, input().split())
        aldo += jog_um
        beto += jog_dois
    print("Teste", test)
    if aldo > beto:
        print("Aldo")
    else:
        print("Beto")
    print()