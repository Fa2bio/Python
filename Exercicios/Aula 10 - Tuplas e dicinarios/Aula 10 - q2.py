__author__ = 'Fabio'

def dicionario():
    turma = {}
    loop = True
    while loop is True:
        aluno = input("Digite o nome do aluno: ")
        if aluno != "":
            nota1 = eval(input("Digite a primeira nota: "))
            nota2 = eval(input("Digite a primeira nota: "))
            turma[aluno] = [nota1, nota2]
        else:
            loop = False
    return turma


def media(x):
    aluno = input("Digite o nome do aluno, para calcular a media: ")
    media = 0
    for i in x[aluno]:
        media += i/2
    return media
print(media(dicionario()))
