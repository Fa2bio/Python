__author__ = 'Fabio'
import operator


def dicionario():
    karts = {}
    for i in range(6):
        tempo = []
        nome = input("Digite o nome do corredor: ")
        for n in range(10):
            tempo.append(eval(input("Digite o tempo da volta: ")))
        karts[nome] = tempo
    return karts


def menor_tempo(x):
    classificacao = {}
    for nome in x:
        menor_lista = x[nome]
        menor = menor_lista[0]
        for z in range(len(menor_lista)):
            if menor_lista[z] < menor:
                menor = menor_lista[z]
            classificacao[nome] = [menor]
    return classificacao


def ordenar(a):
    ordenada = sorted(a.items(), key=operator.itemgetter(1))
    return ordenada

print(ordenar(menor_tempo(dicionario())))
