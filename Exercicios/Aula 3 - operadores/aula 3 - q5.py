__author__ = 'Fabio'
data = eval(input('Digite a data de nascimento: '))
mes = input('Digite o mes de nascimento: ')

if (mes == 'março' or mes == 'Março' or mes == 'MARÇO') and (data >= 21 and data <=31) or (mes == 'abril' or mes == 'Abril' or mes == 'ABRIL') and (data >= 1 and data <= 20):
    print ('O signo é Aries')

if (mes == 'abril' or mes == 'Abril' or mes == 'ABRIL') and (data >= 21 and data <=30) or (mes == 'maio' or mes == 'Maio' or mes == 'MAIO') and (data >= 1 and data <= 20):
    print ('O signo é Touro')

if (mes == 'maio' or mes == 'Maio' or mes == 'MAIO') and (data >= 21 and data <=31) or (mes == 'junho' or mes == 'Junho' or mes == 'JUNHO') and (data >= 1 and data <= 20):
    print ('O signo é Gêmeos')

if (mes == 'junho' or mes == 'Junho' or mes == 'JUNHO') and (data >= 21 and data <=30) or (mes == 'julho' or mes == 'Julho' or mes == 'JULIO') and (data >= 1 and data <= 21):
    print ('O signo é Câncer')

if (mes == 'julho' or mes == 'Julho' or mes == 'JULHO') and (data >= 22 and data <=31) or (mes == 'agosto' or mes == 'Agosto' or mes == 'AGOSTO') and (data >= 1 and data <= 22):
    print ('O signo é Leão')

if (mes == 'agosto' or mes == 'Agosto' or mes == 'AGOSTO') and (data >= 23 and data <=31) or (mes == 'setembro' or mes == 'Setembro' or mes == 'SETEMBRO') and (data >= 1 and data <= 22):
    print ('O signo é Virgem')

if (mes == 'setembro' or mes == 'Setembro' or mes == 'SETEMBRO') and (data >= 23 and data <=30) or (mes == 'outubro' or mes == 'Outubro' or mes == 'OUTUBRO') and (data >= 1 and data <= 22):
    print ('O signo é Libra')

if (mes == 'outubro' or mes == 'Outubro' or mes == 'OUTUBRO') and (data >= 23 and data <=31) or (mes == 'novembro' or mes == 'Novembro' or mes == 'NOVEMBRO') and (data >= 1 and data <= 21):
    print ('O signo é Escorpião')

if (mes == 'novembro' or mes == 'Novembro' or mes == 'NOVEMBRO') and (data >= 22 and data <=30) or (mes == 'dezembro' or mes == 'Dezembro' or mes == 'DEZEMBRO') and (data >= 1 and data <= 21):
    print ('O signo é Sagitário')

if (mes == 'dezembro' or mes == 'Dezembro' or mes == 'DEZEMBRO') and (data >= 22 and data <=31) or (mes == 'janeiro' or mes == 'Janeiro' or mes == 'JANEIRO') and (data >= 1 and data <= 20):
    print ('O signo é Capricónio')

if (mes == 'janeiro' or mes == 'Janeiro' or mes == 'JANEIRO') and (data >= 21 and data <=31) or (mes == 'fevereiro' or mes == 'Fevereiro' or mes == 'FEVEREIRO') and (data >= 1 and data <= 19):
    print ('O signo é Aquario')

if (mes == 'fevereiro' or mes == 'Fevereiro' or mes == 'FEVEREIRO') and (data >= 20 and data <=29) or (mes == 'março' or mes == 'Março' or mes == 'MARÇO') and (data >= 1 and data <= 20):
    print ('O signo é Peixes')