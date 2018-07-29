numero = int(input("Digite um número entre 0 e 9999:"))
mil = numero // 1000
cem = numero % 1000 // 100
dez = numero % 1000 % 100 // 10
uni = numero % 1000 % 100 % 10

if mil!=0:
    if mil==1:
        dig_mil= 'Mil'
    elif mil==2:
        dig_mil= 'Dois mil'
    elif mil==3:
        dig_mil= 'Três mil'
    elif mil==4:
        dig_mil= 'Quatro mil'
    elif mil==5:
        dig_mil= 'Cinco mil'
    elif mil==6:
        dig_mil= 'Seis mil'
    elif mil==7:
        dig_mil= 'Sete mil'
    elif mil==8:
        dig_mil= 'Oito mil'
    elif mil==9:
        dig_mil= 'Nove mil'
else:
    dig_mil= ''

if mil==0 and cem==1 and dez==0 and uni==0:
    dig_cem= 'Cem'

elif mil!=0 and cem!=0 and dez==0 and uni==0:
    if cem==1:
        dig_cem= 'e cem'
    elif cem==2:
        dig_cem= 'e duzentos'
    elif cem==3:
        dig_cem= 'e trezentos'
    elif cem==4:
        dig_cem= 'e quatrocentos'
    elif cem==5:
        dig_cem= 'e quinhentos'
    elif cem==6:
        dig_cem= 'e seicentos'
    elif cem==7:
        dig_cem= 'e setecentos'
    elif cem==8:
        dig_cem= 'e oitocentos'
    elif cem==9:
        dig_cem= 'e novecentos'

elif cem!=0 and mil!=0:
    if cem==1:
        dig_cem= 'cento'
    elif cem==2:
        dig_cem= 'duzentos'
    elif cem==3:
        dig_cem= 'trezentos'
    elif cem==4:
        dig_cem= 'quatrocentos'
    elif cem==5:
        dig_cem= 'quinhentos'
    elif cem==6:
        dig_cem= 'seiscentos'
    elif cem==7:
        dig_cem= 'setecentos'
    elif cem==8:
        dig_cem= 'oitocentos'
    elif cem==9:
        dig_cem= 'novecentos'

elif cem!=0 and mil==0:
    if cem==1:
        dig_cem= 'Cento'
    elif cem==2:
        dig_cem= 'Duzentos'
    elif cem==3:
        dig_cem= 'Trezentos'
    elif cem==4:
        dig_cem= 'Quatrocentos'
    elif cem==5:
        dig_cem= 'Quinhentos'
    elif cem==6:
        dig_cem= 'Seiscentos'
    elif cem==7:
        dig_cem= 'Setecentos'
    elif cem==8:
        dig_cem= 'Oitocentos'
    elif cem==9:
        dig_cem= 'Novecentos'

else:
    dig_cem= ''

if dez!=0 and mil!=0 or cem!=0:
    if dez==1:
        if uni==0:
            dig_dez= 'e dez'
        elif uni==1:
            dig_dez= 'e onze'
        elif uni==2:
            dig_dez= 'e doze'
        elif uni==3:
            dig_dez= 'e treze'
        elif uni==4:
            dig_dez= 'e quatorze'
        elif uni==5:
            dig_dez= 'e quinze'
        elif uni==6:
            dig_dez= 'e dezesseis'
        elif uni==7:
            dig_dez= 'e dezessete'
        elif uni==8:
            dig_dez= 'e dezoito'
        elif uni==9:
            dig_dez= 'e dezenove'
    elif dez==2:
        dig_dez= 'e vinte'
    elif dez==3:
        dig_dez= 'e trinta'
    elif dez==4:
        dig_dez= 'e quarenta'
    elif dez==5:
        dig_dez= 'e cinquenta'
    elif dez==6:
        dig_dez= 'e sessenta'
    elif dez==7:
        dig_dez= 'e setenta'
    elif dez==8:
        dig_dez= 'e oitenta'
    elif dez==9:
        dig_dez= 'e noventa'

elif dez!=0 and mil==0 and cem==0:
    if dez==1:
        if uni==0:
            dig_dez= 'Dez'
        elif uni==1:
            dig_dez= 'Onze'
        elif uni==2:
            dig_dez= 'Doze'
        elif uni==3:
            dig_dez= 'Treze'
        elif uni==4:
            dig_dez= 'Quatorze'
        elif uni==5:
            dig_dez= 'Quinze'
        elif uni==6:
            dig_dez= 'Dezesseis'
        elif uni==7:
            dig_dez= 'Dezessete'
        elif uni==8:
            dig_dez= 'Dezoito'
        elif uni==9:
            dig_dez= 'Dezenove'
    elif dez==2:
        dig_dez= 'Vinte'
    elif dez==3:
        dig_dez= 'Trinta'
    elif dez==4:
        dig_dez= 'Quarenta'
    elif dez==5:
        dig_dez= 'Cinquenta'
    elif dez==6:
        dig_dez= 'Sessenta'
    elif dez==7:
        dig_dez= 'Setenta'
    elif dez==8:
        dig_dez= 'Oitenta'
    elif dez==9:
        dig_dez= 'Noventa'
else:
    dig_dez= ''

if uni!=0 and dez>1 or mil!=0 and dez==0 or mil==0 and cem!=0 and dez==0:
    if uni==1:
        dig_uni= 'e um'
    elif uni==2:
        dig_uni= 'e dois'
    elif uni==3:
        dig_uni= 'e três'
    elif uni==4:
        dig_uni= 'e quatro'
    elif uni==5:
        dig_uni= 'e cinco'
    elif uni==6:
        dig_uni= 'e seis'
    elif uni==7:
        dig_uni= 'e sete'
    elif uni==8:
        dig_uni= 'e oito'
    elif uni==9:
        dig_uni= 'e nove'

elif uni!=0 and mil==0 and cem==0 and dez==0:
    if uni==1:
        dig_uni= 'Um'
    elif uni==2:
        dig_uni= 'Dois'
    elif uni==3:
        dig_uni= 'Três'
    elif uni==4:
        dig_uni= 'Quatro'
    elif uni==5:
        dig_uni= 'Cinco'
    elif uni==6:
        dig_uni= 'Seis'
    elif uni==7:
        dig_uni= 'Sete'
    elif uni==8:
        dig_uni= 'Oito'
    elif uni==9:
        dig_uni= 'Nove'
else:
    dig_uni= ''


if mil==0 and cem==0 and dez==0 and uni!=0:
    print(dig_uni)
elif mil==00 and cem==0 and dez!=0 and uni==0:
    print(dig_dez)
elif mil==0 and cem==0 and dez!=0 and uni!=0:
    print(dig_dez, dig_uni)
elif mil==0 and cem!=0 and dez==0 and uni==0:
    print(dig_cem)
elif mil==0 and cem!=0 and dez==0 and uni!=0:
    print(dig_cem, dig_uni)
elif mil==0 and cem!=0 and dez!=0 and uni==0:
    print(dig_cem, dig_dez)
elif mil==0 and cem!=0 and dez!=0 and uni!=0:
    print(dig_cem, dig_dez, dig_uni)
elif mil!=0 and cem==0 and dez==0 and uni==0:
    print(dig_mil)
elif mil!=0 and cem==0 and dez==0 and uni!=0:
    print(dig_mil, dig_uni)
elif mil!=0 and cem==0 and dez!=0 and uni==0:
    print(dig_mil, dig_dez)
elif mil!=0 and cem==0 and dez!=0 and uni!=0:
    print(dig_mil, dig_dez, dig_uni)
elif mil!=0 and cem!=0 and dez==0 and uni==0:
    print(dig_mil, dig_cem)
elif mil!=0 and cem!=0 and dez==0 and uni!=0:
    print(dig_mil, dig_cem, dig_uni)
elif mil!=0 and cem!=0 and dez!=0 and uni==0:
    print(dig_mil, dig_cem, dig_dez)
elif mil!=0 and cem!=0 and dez!=0 and uni!=0:
    print(dig_mil, dig_cem, dig_dez, dig_uni)
elif mil==0 and cem==0 and dez==0 and uni==0:
    print('Zero')