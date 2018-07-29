author__ = 'Fabio'
dia_antigo = 1
dia_velho = 365
ano_velho = 1
soma_ano_antigo = 0
mes_velho = 0
contador_mes_velho = 0
dia_recente = 365
ano_recente = 1
soma_ano_novo = 0
mes_recente = 0
contador_mes_recente = 0
while dia_antigo != 0 :
  dia_antigo = eval(input('Digite o dia da primeira data :'))
  mes_antigo = eval(input('Digite o mes da primeira data :'))
  ano_antigo = eval(input('Digite o ano da primeira data :'))
  dia_novo = eval(input('Digite o dia da segunda data :'))
  mes_novo = eval(input('Digite o mes da segunda data :'))
  ano_novo = eval(input('Digite o ano da segunda data :'))
  if ano_velho%4 == 0:
      dia_velho = 366
  elif ano_velho%100 == 0 and ano_velho%400 != 0:
      dia_velho = 365
  while ano_velho < ano_antigo:
      soma_ano_antigo = soma_ano_antigo + dia_velho
      ano_velho = ano_velho + 1
  if contador_mes_velho == 1 or contador_mes_velho == 3 or contador_mes_velho == 5 or contador_mes_velho == 7 or contador_mes_velho == 8 or contador_mes_velho == 10 or contador_mes_velho == 12:
      mes_velho = 31
  if contador_mes_velho == 4 or contador_mes_velho == 6 or contador_mes_velho == 9 or contador_mes_velho == 11 :
      mes_velho = 30
  if contador_mes_velho == 2 and dia_velho == 365:
      mes_velho = 28
  if contador_mes_velho == 2 and dia_velho == 366:
      mes_velho = 29
  while contador_mes_velho < mes_antigo:
      soma_ano_antigo = soma_ano_antigo + mes_velho
      contador_mes_velho = contador_mes_velho + 1
  soma_ano_antigo = soma_ano_antigo + dia_antigo
  if ano_recente%4 == 0:
      dia_recente = 366
  elif ano_recente%100 == 0 and ano_recente%400 != 0:
      dia_recente = 365
  while ano_recente < ano_novo:
      soma_ano_novo = soma_ano_novo + dia_recente
      ano_recente = ano_recente + 1
  if contador_mes_recente == 1 or contador_mes_recente == 3 or contador_mes_recente == 5 or contador_mes_recente == 7 or contador_mes_recente == 8 or contador_mes_recente == 10 or contador_mes_recente == 12:
      mes_recente = 31
  if contador_mes_recente == 4 or contador_mes_recente == 6 or contador_mes_recente == 9 or contador_mes_recente == 11 :
      mes_recente = 30
  if contador_mes_recente == 2 and dia_recente == 365:
      mes_recente = 28
  if contador_mes_recente == 2 and dia_recente == 366:
      mes_recente = 29
  while contador_mes_recente < mes_novo:
      soma_ano_novo = soma_ano_novo + mes_recente
      contador_mes_recente = contador_mes_recente + 1
  soma_ano_novo = soma_ano_novo + dia_novo
  calculoano = soma_ano_novo - soma_ano_antigo
  print(calculoano)