def menu(matriz):
    for i in range(len(matriz)):
        print(matriz[i])
    return 'Este são os produtos e os preços da sorveteria'

def vendas():
    print(menu(matriz))
    print()

    controle = True
    cont = 0
    while controle:
        escol = input('Digite o cógido do produto ou deixe este campo em branco: ').lower()
        if escol != '':
            if escol == 'a':
                cont += 3.5

            elif escol == 'b':
                cont += 4

            elif escol == 'c':
                cont += 5.5

            elif escol == 'd':
                cont += 7.5

            elif escol == 'e':
                cont += 9

        else:
            controle = False
        total(escol)

    print('O total desta venda foi R$',cont)
    print()

def total(escol):
    total = 0
    cont_a = 0
    cont_b = 0
    cont_c = 0
    cont_d = 0
    cont_e = 0

    total_a = 0
    total_b = 0
    total_c = 0
    total_d = 0
    total_e = 0

    if escol == 'a':
        cont_a += 1
        total_a += 3.5

    elif escol == 'b':
        cont_b += 1
        total_b += 4

    elif escol == 'c':
        cont_c += 1
        total_c += .5

    elif escol == 'd':
        cont_d += 1
        total_d += 7.5

    elif escol == 'e':
        cont_e += 1
        total_e += 9
        total += cont

def relatorio(a):

    print('O total de refrigerantes vendidos foi:',cont_a)
    print('O total de casquinhas simples vendidos foi:',cont_b)
    print('O total de casquinhas dupla vendidos foi:',cont_c)
    print('O total de sundae vendidos foi:',cont_d)
    print('O total de banana split vendidos foi:',cont_e)

    print('O total arrecadado com os refrigerantes foi:',total_a)
    print('O total arrecadado com as casquinhas simples foi:',total_b)
    print('O total arrecadado com as casquinhas dupla foi:',total_c)
    print('O total arrecadado com os sundae foi:',total_d)
    print('O total total arrecadado com as bananas split foi:',total_e)

    print('O total arrecadado foi',total)



matriz = [['|Código| Produto| Preço|'],['|A| |Refrigerante| |3.5|'],['|B| |Casquinha Simples| |4.0|'],['|C| |Casquinha Dupla| |5.5|'],['|D| |Sundae| |7.5|'],['|E| |Banana Split| |9.0|']]

loop = True
while loop:
    info = input('Deseja comprar algo ?(S/N): ').lower()
    if info == 'n':
        loop = False

    else:
        vendas()