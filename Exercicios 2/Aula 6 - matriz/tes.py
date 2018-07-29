loop = True
agenda = []
nomes = []

while loop is True:
    x = input('Digite "a" para adicionar telefones, digite "b" para procurar um telefone ou digite "sair": ')
    if x == 'sair' or x == 'Sair' or x == 'SAIR':
        loop = False
    else:
        if x == 'a' or x == 'A':
            cont = 0
            repe = eval(input('Quantos números você deseja adicionar a esta agenda ?: '))
            while cont != repe:
                nomes = []
                nomes.append(input('Digite o nome: '))
                nomes.append(input('Digite o número do telefone: '))
                agenda.append(nomes)
                agenda.sort()
                cont += 1
                print (agenda)

        if x == 'b' or x == 'B':
            controle = False
            y = input('Digite o nome que deseja procurar: ')
            for i in range(len(agenda)):
                for j in range(len(agenda)):
                    if not(controle) and y in agenda[i][0]:
                        print('O número do(a)',y,'é',agenda[i][1])
                        controle = True
                    elif not(controle) and y < agenda[i][0]:
                        print('O nome não esta na agenda')
                        controle = True