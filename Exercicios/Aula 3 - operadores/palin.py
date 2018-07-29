num = int(input('Digite o numero com 5 digitos: '))
a = num//10000 #5
num = num%10000
b = num//1000 #4
num = num%1000
c = num//100 #3
num = num%100 #2
d = num//10
num = num%10
e = num #1

if a == e and b == d:
    print ('São palindromos')
else:
    print ('Não são palindromos')
