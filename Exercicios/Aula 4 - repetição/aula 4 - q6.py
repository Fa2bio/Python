num = int(input("Digite quantos números perfeitos você quer (o programa só calcula com eficiencia até 4): "))
num_1 = 2
qtd_nums = 0
while qtd_nums != num:
    soma = 1
    for i in range(2, num_1):
        if num_1 % i == 0:
            soma += i
    if soma == num_1:
        print(num_1)
        qtd_nums += 1
    num_1 += 1