fila = []
aluno = True

while aluno == True:
    controle = True
    while controle == True:
        entra = input('Digite a matricula do aluno ou deixe este campo em branco: ')
        if entra == '':
            controle = False
        else:
            fila.append(entra)

    if len(fila) > 0:
        for i in range(len(fila)-1,-1,-1):
            print(fila[i],'Você esta guardando lugar na fila para seus amigos ?')
            guardar = input('(S/N): ').lower()

            if guardar == 's':
                quant = eval(input('Para quantos amigos ?: '))
                for k in range(quant):
                    aluno_1 = input('Qual a matricula deste seu amigo ?: ')
                    pos = i + 1
                    fila.insert(pos,aluno_1)

            continu = input('Você irá continuar na fila ? (S/N): ').lower()

            if continu == 'n':
                pos = fila.index(fila[i])
                fila.pop(pos)

    aluno = False
    esco = input('Já são 11 hrs ?(S/N): ').lower()
    if esco == 'n':
        esco_1 = input('Ainda existem alunos para entrar na fila ? (S/N): ').lower()
        if esco_1 == 's':
            aluno = True
        else:
            aluno = False
            print()
            if len(fila) > 300:
                i = len(fila)
                while i > 0:
                    i -= 1
                    if i > 299:
                        fila.remove(fila[i])

            if len(fila) != 0:
                print(len(fila), 'alunos comerão no bandejão')
                print('Os alunos', fila, 'conseguiram senha')

            if len(fila) == 0:
                print('Ninguem quis comer no bandejão hoje')
    else:
        aluno = False
        print()
        print('A fila foi congelada')
        if len(fila) > 300:
            i = len(fila)
            while i > 0:
                i -= 1
                if i > 299:
                    fila.remove(fila[i])

        if len(fila) != 0:
            print(len(fila), 'alunos comerão no bandejão')
            print('Os alunos', fila, 'conseguiram senha')

        elif len(fila) == 0:
            print('Ninguem quis comer no bandejão hoje')

