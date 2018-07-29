def primeiro(cpf):
    multi = 10
    acumulador = 0
    for i in range(len(cpf)):
        if i != len(cpf) - 1 and i != len(cpf) - 2:
            try:
                x = int(cpf[i])
                acumulador += x * multi
                multi -= 1
            except ValueError:
                pass
    try:
        acumulador = (acumulador * 10) % 11
        if acumulador == 10:
            acumulador = 0

        if acumulador == int(cpf[len(cpf) - 2]):
            valido = True
        else:
            valido = False
        return valido
    except ValueError:
        valido = False
        return valido

def segundo(cpf):
    a = primeiro(cpf)
    multi = 11
    acumulador = 0
    for i in range(len(cpf)):
        try:
            if i != len(cpf) - 1:
                x = int(cpf[i])
                acumulador += x * multi
                multi -= 1
        except ValueError:
            pass
    acumulador = (acumulador * 10) % 11
    if acumulador == 10:
        acumulador = 0

    if acumulador == int(cpf[len(cpf) - 1]) and a:
        return True
    else:
        return False

cpf = input('Digite o cpf (somente números): ')

print(segundo(cpf))