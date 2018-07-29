__author__ = 'Fabio'
numero = eval(input("Escreva um número inteiro entre 0 e 9999:"))
m = numero // 1000
c = numero % 1000 // 100
d = numero % 1000 % 100 // 10
u = numero % 1000 % 100 % 10

if m!=0:
    if m==1:
        mv='Mil'
    elif m==2:
        mv='Dois mil'
    elif m==3:
        mv='Três mil'
    elif m==4:
        mv='Quatro mil'
    elif m==5:
        mv='Cinco mil'
    elif m==6:
        mv='Seis mil'
    elif m==7:
        mv='Sete mil'
    elif m==8:
        mv='Oito mil'
    elif m==9:
        mv='Nove mil'
else:
    mv=''

if m==0 and c==1 and d==0 and u==0:
    cv='Cem'

elif m!=0 and c!=0 and d==0 and u==0:
    if c==1:
        cv='e cem'
    elif c==2:
        cv='e duzentos'
    elif c==3:
        cv='e trezentos'
    elif c==4:
        cv='e quatrocentos'
    elif c==5:
        cv='e quinhentos'
    elif c==6:
        cv='e seicentos'
    elif c==7:
        cv='e setecentos'
    elif c==8:
        cv='e oitocentos'
    elif c==9:
        cv='e novecentos'

elif c!=0 and m!=0:
    if c==1:
        cv='cento'
    elif c==2:
        cv='duzentos'
    elif c==3:
        cv='trezentos'
    elif c==4:
        cv='quatrocentos'
    elif c==5:
        cv='quinhentos'
    elif c==6:
        cv='seiscentos'
    elif c==7:
        cv='setecentos'
    elif c==8:
        cv='oitocentos'
    elif c==9:
        cv='novecentos'

elif c!=0 and m==0:
    if c==1:
        cv='Cento'
    elif c==2:
        cv='Duzentos'
    elif c==3:
        cv='Trezentos'
    elif c==4:
        cv='Quatrocentos'
    elif c==5:
        cv='Quinhentos'
    elif c==6:
        cv='Seiscentos'
    elif c==7:
        cv='Setecentos'
    elif c==8:
        cv='Oitocentos'
    elif c==9:
        cv='Novecentos'

else:
    cv=''

if d!=0 and m!=0 or c!=0:
    if d==1:
        if u==0:
            dv='e dez'
        elif u==1:
            dv='e onze'
        elif u==2:
            dv='e doze'
        elif u==3:
            dv='e treze'
        elif u==4:
            dv='e quatorze'
        elif u==5:
            dv='e quinze'
        elif u==6:
            dv='e dezesseis'
        elif u==7:
            dv='e dezessete'
        elif u==8:
            dv='e dezoito'
        elif u==9:
            dv='e dezenove'
    elif d==2:
        dv='e vinte'
    elif d==3:
        dv='e trinta'
    elif d==4:
        dv='e quarenta'
    elif d==5:
        dv='e cinquenta'
    elif d==6:
        dv='e sessenta'
    elif d==7:
        dv='e setenta'
    elif d==8:
        dv='e oitenta'
    elif d==9:
        dv='e noventa'

elif d!=0 and m==0 and c==0:
    if d==1:
        if u==0:
            dv='Dez'
        elif u==1:
            dv='Onze'
        elif u==2:
            dv='Doze'
        elif u==3:
            dv='Treze'
        elif u==4:
            dv='Quatorze'
        elif u==5:
            dv='Quinze'
        elif u==6:
            dv='Dezesseis'
        elif u==7:
            dv='Dezessete'
        elif u==8:
            dv='Dezoito'
        elif u==9:
            dv='Dezenove'
    elif d==2:
        dv='Vinte'
    elif d==3:
        dv='Trinta'
    elif d==4:
        dv='Quarenta'
    elif d==5:
        dv='Cinquenta'
    elif d==6:
        dv='Sessenta'
    elif d==7:
        dv='Setenta'
    elif d==8:
        dv='Oitenta'
    elif d==9:
        dv='Noventa'
else:
    dv=''

if u!=0 and d>1 or m!=0 and d==0 or m==0 and c!=0 and d==0:
    if u==1:
        uv='e um'
    elif u==2:
        uv='e dois'
    elif u==3:
        uv='e três'
    elif u==4:
        uv='e quatro'
    elif u==5:
        uv='e cinco'
    elif u==6:
        uv='e seis'
    elif u==7:
        uv='e sete'
    elif u==8:
        uv='e oito'
    elif u==9:
        uv='e nove'

elif u!=0 and m==0 and c==0 and d==0:
    if u==1:
        uv='Um'
    elif u==2:
        uv='Dois'
    elif u==3:
        uv='Três'
    elif u==4:
        uv='Quatro'
    elif u==5:
        uv='Cinco'
    elif u==6:
        uv='Seis'
    elif u==7:
        uv='Sete'
    elif u==8:
        uv='Oito'
    elif u==9:
        uv='Nove'
else:
    uv=''


if m==0 and c==0 and d==0 and u!=0:
    print(uv)
elif m==00 and c==0 and d!=0 and u==0:
    print(dv)
elif m==0 and c==0 and d!=0 and u!=0:
    print(dv,uv)
elif m==0 and c!=0 and d==0 and u==0:
    print(cv)
elif m==0 and c!=0 and d==0 and u!=0:
    print(cv,uv)
elif m==0 and c!=0 and d!=0 and u==0:
    print(cv,dv)
elif m==0 and c!=0 and d!=0 and u!=0:
    print(cv,dv,uv)
elif m!=0 and c==0 and d==0 and u==0:
    print(mv)
elif m!=0 and c==0 and d==0 and u!=0:
    print(mv,uv)
elif m!=0 and c==0 and d!=0 and u==0:
    print(mv,dv)
elif m!=0 and c==0 and d!=0 and u!=0:
    print(mv,dv,uv)
elif m!=0 and c!=0 and d==0 and u==0:
    print(mv,cv)
elif m!=0 and c!=0 and d==0 and u!=0:
    print(mv,cv,uv)
elif m!=0 and c!=0 and d!=0 and u==0:
    print(mv,cv,dv)
elif m!=0 and c!=0 and d!=0 and u!=0:
    print(mv,cv,dv,uv)
elif m==0 and c==0 and d==0 and u==0:
    print('Zero')