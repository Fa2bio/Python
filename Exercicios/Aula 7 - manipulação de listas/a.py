loop = True
agenda = []
nomes = []

while loop is True:
    pos = 0
    achou = False
    cont = 0
    g = 0
    controle = False
    x = input('Digite "a" para adicionar telefones, digite "b" para procurar um telefone ou digite "sair": ')
    if x == 'sair' or x == 'Sair' or x == 'SAIR':
        loop = False

    else:
        if x == 'a' or x == 'A':
            repe = eval(input('Quantos números você deseja adicionar a esta agenda ?: '))
            while cont != repe:
                nomes = []
                nomes.append(input('Digite o nome: '))
                nomes.append(input('Digite o número do telefone: '))
                agenda.append(nomes)
                agenda.sort()
                cont += 1
        elif x == 'b' or x == 'B':
            print(agenda)
            y = input('Digite o nome que deseja procurar: ')
            nome = y
            while pos < len(agenda):
                if nome < agenda[pos][0]:
                    if nome == agenda[pos][0]:
                        print(agenda[pos][1])
                    pos = len(agenda)
                else:
                    pos = pos + 1
                    print(agenda[g])

