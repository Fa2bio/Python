__author__ = 'Fabio'
def extenso (data):
    mes = {1:'Janeiro',2:'Fevereiro',3:'Março',4:'Abril',5:'Maio',6:'Junho',7:'Julho',8:'Agosto',9:'Setembro',10:'Outubro',11:'Novembro',12:'Dezembro'}
    separador = data.split("/")
    print ('Você nasceu em',separador[0],' de ',mes[int(separador[1])],' de ',separador[2])

data = input('Digite uma data: ')
print(extenso(data))



