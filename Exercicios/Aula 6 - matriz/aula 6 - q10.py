#grupo Fabio da Silva Correa e João Victor Schiavo
M =[]
turma = []
alunos_tur_1 = []
alunos_tur_2 = []

media_turma_1 = 0
media_turma_2 = 0

cont = 0
cont_0 = 0
cont_1 = 0
cont_2 = 0
#gera a turma
for i in range(2):
    #gera os alunos
    aluno = []
    for j in range(3):
        linha = []
        #gera as notas
        media = 0
        for k in range(3):
            if (i == 0) and (cont == 0):
                print('ESTA É A TURMA 1')
                cont += 1
            elif (i == 1) and (cont_0 == 0):
                print()
                print('ESTA É A TURMA 2')
                cont_0 += 1
            if k == 0:
                linha.append(input('Digite o nome do aluno: '))
            else:
                num = eval(input('Digite a nota: '))
                linha.append(num)
                media += num
                if k == 2:
                    media = media / 2
                    linha.append(media)
                #gera a media das turmas
                if i == 0:
                    media_turma_1 += num
                if i == 1:
                    media_turma_2 += num
        aluno.append(linha)
    M.append(aluno)
    #adc ao vetor TURMA as medias
    if i == 0:
        turma.append(media_turma_1)
    if i == 1:
        turma.append(media_turma_2)

#gera a média das turmas
media_turma_1 /= 6
media_turma_2 /= 6
if media_turma_1 > media_turma_2:
    print()
    print('A turma 1 teve a maior média')

elif media_turma_1 == media_turma_2:
    print()
    print('As turmas tem a mesma média')

else:
    print()
    print('A turma 2 teve a maior média')

#gera os alunos que tiveram nota acima da média
for i in range(2):
    for j in range(3):
        for k in range(4):
            if (i == 0) and (k != 0):
                if (M[i][j][3] > media_turma_1) and (M[0][j][0] != alunos_tur_1):
                    alunos_tur_1 = M[0][j][0]
                    print('O aluno da turma 1 que tive nota acima da média de sua turma é o (a):', alunos_tur_1)
                    cont_1 += 1

            if (i == 1) and (k != 0) and (M[1][j][0] != alunos_tur_2):
                if (M[i][j][3] > media_turma_2):
                    alunos_tur_2 = M[1][j][0]
                    print('O aluno da turma 2 que tive nota acima da média de sua turma é o(a):', alunos_tur_2)
                    cont_2 += 1

#gera o erro caso não tenham alunos com nota acima da média da turma
if cont_1 == 0:
    print('Na turma 1, não tiveram alunos com notas acima da média')

if cont_2 == 0:
    print('Na turma 2, não tiveram alunos com notas acima da média')
