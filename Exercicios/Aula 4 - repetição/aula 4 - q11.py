loop = True

cont_nit = 0
cont_pessoas = 0
cont_flu = 0
cont_fla = 0
cont_bota = 0
cont_vas = 0
cont_outros = 0

media_flu = 0
media_fla = 0
media_vas = 0
media_bota = 0
media_outros = 0

while loop is True:
    clube = input('Entre com o número do seu clube (1 – Flamengo, 2 – Vasco,3 – Fluminense, 4 – Botafogo, 5 – Outros) ou deixe este campo em branco: ')
    if clube != '':
        sal = eval(input('Qual o seu salario: '))
        cid = input('Qual a sua cidade natal (1 - Para Niteroi, 2 - Para outra): ')
        cont_pessoas += 1
        if clube == '1':
            cont_fla += 1
            media_fla = (media_fla + sal)/cont_fla
        if clube == '2':
            cont_vas += 1
            media_vas = (media_vas + sal)/cont_vas
        if clube == '3':
            cont_flu += 1
            media_flu = (media_flu + sal)/cont_flu
        if clube == '4':
            cont_bota += 1
            media_bota = (media_bota + sal)/cont_bota
        if clube == '5':
            cont_outros += 1
            media_outros = (media_outros + sal)/cont_outros
        if cid == '1' and clube == '5':
            cont_nit += 1
    else:
        loop = False

print ('O número de torcedores do Flamengo é:',cont_fla)
print ('O número de torcedores do Vasco é:',cont_vas)
print ('O número de torcedores do Fluminense é:',cont_flu)
print ('O número de torcedores do Botafogo é:',cont_bota)
print ('O número de torcedores de outros times é:',cont_outros)

print ('A média salarial dos torcedores do Flamengo é:',media_fla)
print ('A média salarial dos torcedores do Vasco é:',media_vas)
print ('A média salarial dos torcedores do Fluminense é:',media_flu)
print ('A média salarial dos torcedores do Botafogo',media_bota)

print ('O número de pessoas nascidas em Niterói e que não torcem para nenhum dos principais clubes do Rio é:',cont_nit)
print ('O número de pessoas entrevistadas foi:',cont_pessoas)
