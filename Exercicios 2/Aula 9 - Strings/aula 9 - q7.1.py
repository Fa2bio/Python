# Reversão de nome + Letra maiscula


def string_original():
    palavra = input("Digite seu nome: ")
    return palavra


def string_manipulada(a):
    b = a[::-1].upper()
    print(b)
string_manipulada(string_original())
