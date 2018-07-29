__author__ = 'Fabio'
def hora_certa(a):
    if 0 < h > 24:
        return False
    else:
        return True


def horas(a):
    if 12 < h:
        return h - 12
    else:
        return horas


def minutos(a):
    if 0 < m > 60:
        return False
    else:
        return True


def momento(a):
    if h > 12:
        return "P.M"
    else:
        return "A.M"


verificar = True
while verificar:
    end = input("Digite END para fechar ou aperte ENTER para continuar.")
    if end == "END" or end == "end":
        verificar = False
    else:
        h = int(eval(input("Digite as horas: ")))
        m = int(eval(input("Digite os minutos: ")))
        if hora_certa(h) == False or minutos(m) == False:
            print("NULL")
        else:
            print(horas(h), ":", m, momento(h))
