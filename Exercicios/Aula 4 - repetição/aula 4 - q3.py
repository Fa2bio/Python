__author__ = 'Fabio'
num = int(input("Digite o valor de n: "))
f_ant = 0
f_atual = 1
i = 1
print(f_ant)
print(f_atual)
while i < num: # antes da comparação vale que f_atual == F(i)
    f_prox  = f_ant + f_atual
    f_ant   = f_atual
    f_atual = f_prox
    i = i + 1
    print(f_atual)