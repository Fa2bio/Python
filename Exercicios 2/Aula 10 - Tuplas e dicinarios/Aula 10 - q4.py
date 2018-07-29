__author__ = 'Fabio'
def acrescenta_numero(lisa_tele,nome,telefone):
    lisa_tele[nome] = telefone
    return lisa_tele
def retira_contato(lista_tele,nome):
    if nome in lista_tele:
        del lista_tele[nome]
        return lista_tele
    else:
        print('Contato inexistente')
def procura_numero(lista_tele,nome):
    if nome in lista_tele:
        print(lista_tele[nome])
    else:
        print('Contato inexistente')

def main():
    lista_tele = {}
    while True:
        mostra_menu()
        menu_escolhas = int(input("Escolha a sua opção (1-4): "))
        if menu_escolhas == 1:
            print("Acrescentar Nome e Número")
            nome = input("Nome: ")
            telefone = input("Número: ")
            acrescenta_numero(lista_tele, nome, telefone)
        elif menu_escolhas == 2:
            print("Retira Nome e Número")
            nome = input("Nome: ")
            retira_contacto(lista_tele, nome)
        elif menu_escolhas == 3:
            print("Procura Número")
            nome = input("Nome: ")
            print(procura_numero(lista_tele, nome))
        elif menu_escolhas == 4:
            break
        else:
            mostra_lista()

if __name__ == '__main__':
    main()

def mostra_lista(lista_tele):
    for nome,numero in sorted(lista_tele.items()):
        print()
        print('Nome: %s\nNúmero: %s' %
            (nome,numero))