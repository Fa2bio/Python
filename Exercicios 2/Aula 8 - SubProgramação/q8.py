__author__ = 'Fabio'
def manipular_dia(a, b, c):
    if b == 2 and manipular_ano(c) == True:
        if 1 < a < 30:
            return True
        else:
            return False
    elif b == 2 and manipular_ano(c) == False:
        if 1 < a < 29:
            return True
        else:
            return False
    elif b == 1 or 3 or 5 or 7 or 8 or 10 or 12:
        if 1 < a < 32:
            return True
        else:
            return False
    else:
        if 1 < a < 31:
            return True
        else:
            return False


def manipular_mes(a):
    if 0 < a < 13:
        return True
    else:
        return False


def transformar_mes(a):
    if a == 1:
        return "Janeiro"
    elif a == 2:
        return "Fevereiro"
    elif a == 3:
        return"Março"
    elif a == 4:
        return"Abril"
    elif a == 5:
        return"Maio"
    elif a == 6:
        return"Junho"
    elif a == 7:
        return"Julho"
    elif a == 8:
        return"Agosto"
    elif a == 9:
        return"Setembro"
    elif a == 10:
        return"Outubro"
    elif a == 11:
        return"Novembro"
    elif a == 12:
        return"Dezembro"


def manipular_ano(a):
    if 1 < a < 9999:
        if a % 4 == 0:
            if a % 100 == 0:
                if a % 400 == 0:
                    return True
            else:
                return True
        else:
            return False

verificar = True
while verificar:
    end = input("Digite END para fechar ou aperte ENTER para continuar.")
    if end == "END" or end == "end":
        verificar = False
    else:
        dia = int(eval(input("Digite o dia: ")))
        mes = int(eval(input("Digite o mes: ")))
        ano = int(eval(input("Digite o ano: ")))
        if manipular_dia(dia, mes, ano) == True and manipular_mes(mes) == True and (1 < ano < 9999):
            print(dia, "de", transformar_mes(mes), "de", ano)
        else:
            print("NULL")
