r = int(input())
somador = 7
if 30 >= r > 10:
    somador += r-10
if r > 30 and r <= 100:
    somador += (r-30)*2 + 20
elif r > 100:
    somador += (r-100)*5 + 160
print(somador)