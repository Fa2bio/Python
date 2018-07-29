cap = eval(input('Digite a quantia que você deseja investir: '))
juros = eval(input('Qual o valor da taxa de juros ?: '))
mes = 0
ano = 12
loop = True
bruto = 0

while mes != ano and loop == True:
    if mes == 0:
        total_jurs = cap * (juros/100)
        bruto = bruto + cap + total_jurs
    elif mes != 0:
        bruto = bruto + cap
        total_jurs = bruto * (juros / 100)
        bruto = bruto + total_jurs
    mes += 1
    if mes == 12:
        print('Saldo do investimento após 1 ano: ',round(bruto,2))
        loop = False
        escol = input('Deseja processar mais um ano? (S/N): ')
        if escol == 'S' or escol == 's':
            loop = True
            mes = 0
            cap = eval(input('Digite a quantia que você deseja investir: '))
            juros = eval(input('Qual o valor da taxa de juros ?: '))
