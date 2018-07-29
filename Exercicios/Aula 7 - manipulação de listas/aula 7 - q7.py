#grupo = Fabio da Silva Correa e Luis Sergio
loop = True
agenda = []
while loop is True:
    achou = False
    controle = False
    cont = 0
    g = 0
    menu = input('Digite "A" para adicionar telefones, digite "B" para procurar um telefone ou digite "SAIR": ').lower()
    if menu == 'sair':
        loop = False

    else:
        if menu == 'a':
            repe = eval(input('Quantos números você deseja adicionar a esta agenda ?: '))
            while cont != repe:
                nomes = []
                name = input('Digite o nome: ').lower()
                nomes.append(name)
                nomes.append(input('Digite o número do telefone: '))
                pos = 0
                if len(agenda) == 0: #se a agenda estiver vazia, adc, senão, ordena
                    agenda.append(nomes)
                else:
                    for i in range(len(agenda)):
                        if name > agenda[i][0]:
                            pos = i + 1
                    agenda.insert(pos, nomes)
                cont += 1

        elif menu == 'b':
            compara = input('Digite o nome que deseja procurar: ')
            busca = compara.lower()

            while (g < len(agenda)) and controle == False:
                nome = agenda[g][0].lower()
                #vai comparar apenas a parte da lista em que a string 'nome' possuir a mesma letra inicial da palavra de comparação
                if busca[0] == nome[0]:
                    if busca == nome:  # se achar o nome, para o loop
                        print('O número do(a)', compara, 'é:', agenda[g][1])
                        achou = True
                        controle = True

                    elif busca != nome and achou == False: #se não achar o nome, verifica se a busca é menor, se for, trava o loop e depois incrementa g
                        if busca < nome:
                            print('O número do(a)', compara, 'não esta na agenda')
                            achou = True
                            controle = True
                        g += 1

                elif (busca[0] != nome[0]) and (busca < nome) and (achou == False):
                    print('O número do(a)', compara, 'não esta na agenda')
                    achou = True
                    controle = True

                else:
                    controle = False
                    g += 1
