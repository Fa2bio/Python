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