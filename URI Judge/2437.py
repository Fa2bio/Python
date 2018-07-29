import math
a,b,c,r = map(int,input().split())

vol_caixa = a*b
area_cir = int(3.14*(r**3))
print(area_cir,"a")
print(vol_caixa)
if area_cir > vol_caixa:
    print("N")
