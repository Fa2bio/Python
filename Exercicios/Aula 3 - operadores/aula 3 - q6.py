__author__ = 'Fábio'
numero = eval(input('Digite um numero entre 1 e 10000, para a conversão:'))
mil = numero // 1000
cem = numero % 1000 // 100
dez = numero % 1000 % 100 // 10
uni = numero % 1000 % 100 % 10 // 1

dig_mil = ''
dig_cem = ''
dig_dez = ''
dig_uni = ''

if mil != 0:
    if mil == 1:
        dig_mil = 'M'
    elif mil == 2:
        dig_mil = 'MM'
    elif mil == 3:
        dig_mil = 'MMM'
    elif mil == 4:
        dig_mil = 'IV'
    elif mil == 5:
        dig_mil = 'V-'
    elif mil == 6:
        dig_mil = 'VI-'
    elif mil == 7:
        dig_mil = 'VII-'
    elif mil == 8:
        dig_mil = 'VII-'
    elif mil == 9:
        dig_mil = 'IX-'
    elif mil == 10:
        dig_mil = 'X-'

if cem != 0:
    if cem == 1:
        dig_cem = 'C'
    elif cem == 2:
        dig_cem = 'CC'
    elif cem == 3:
        dig_cem = 'CCC'
    elif cem == 4:
        dig_cem = 'CD'
    elif cem == 5:
        dig_cem = 'D'
    elif cem == 6:
        dig_cem = 'DC'
    elif cem == 7:
        dig_cem = 'DCC'
    elif cem == 8:
        dig_cem = 'DCCC'
    elif cem == 9:
        dig_cem = 'CM'

if dez != 0:
    if dez == 1:
        dig_dez = 'X'
    elif dez == 2:
        dig_dez = 'XX'
    elif dez == 3:
        dig_dez = 'XXX'
    elif dez == 4:
        dig_dez = 'XL'
    elif dez == 5:
        dig_dez = 'L'
    elif dez == 6:
        dig_dez = 'LX'
    elif dez == 7:
        dig_dez = 'LXX'
    elif dez == 8:
        dig_dez = 'LXXX'
    elif dez == 9:
        dig_dez = 'XC'

if uni != 0:
    if uni == 1:
        dig_uni = 'I'
    elif uni == 2:
        dig_uni = 'II'
    elif uni == 3:
        dig_uni = 'III'
    elif uni == 4:
        dig_uni = 'IV'
    elif uni == 5:
        dig_uni = 'V'
    elif uni == 6:
        dig_uni = 'VI'
    elif uni == 7:
        dig_uni = 'VII'
    elif uni == 8:
        dig_uni = 'VIII'
    elif uni == 9:
        dig_uni = 'IX'

print(dig_mil + dig_cem + dig_dez + dig_uni)






