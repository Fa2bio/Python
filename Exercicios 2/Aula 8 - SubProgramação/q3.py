__author__ = 'Fabio'
def somar(x):
    aux = eval(input("Digite um numero: "))
    x[0] += aux
    return x[0]


def subtrair(x):
    aux = eval(input("Digite um numero: "))
    x[0] -= aux
    return x[0]


def multiplicar(x):
    aux = eval(input("Digite um numero: "))
    x[0] *= aux
    return x[0]


def dividir(x):
    aux = eval(input("Digite um numero: "))
    if aux != 0:
        x[0] /= aux
        return x[0]
    else:
        print('Erro de divisão por 0')
        return x[0]


def limpar_memoria(x):
    x[0] = 0
    return x[0]


def sair(x):
    x[0] = False

# =====================================================================================================================#
memoria = [eval(input("Digite o estado da memória: "))]
status = [True]
while status[0]:
    operação = input("(1) Somar, (2) Subtrair, (3) Multiplicar, (4) Dividir, (5) Limpar memória, (6) Sair do programa) = ")
    if operação == "1":
        print(somar(memoria))
        print()
    elif operação == "2":
        print(subtrair(memoria))
        print()
    elif operação == "3":
        print(multiplicar(memoria))
        print()
    elif operação == "4":
        print(dividir(memoria))
        print()
    elif operação == "5":
        print(limpar_memoria(memoria))
        print()
    elif operação == "6":
        sair(status)
