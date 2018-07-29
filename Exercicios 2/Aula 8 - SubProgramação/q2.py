__author__ = 'Fabio'
def verifia_status(nota):
    if nota >= 6:
        x = 'Aprovado'
    elif nota >= 4 and nota <= 6:
        x = 'Verificação suplementar'
    else:
        x = 'Reprovado'
    return x

nota = eval(input('Digite a nota do aluno: '))
print(verifia_status(nota))