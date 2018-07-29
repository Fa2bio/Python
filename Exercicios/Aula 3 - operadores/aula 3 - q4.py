__author__ = 'Fabio'
sal_fixo = eval(input('Digite o valor do salario fixo: '))
vendas = eval(input('Digite o valor das vendas: '))
sal_bonus = 0

if vendas >= 1000 and vendas <= 5000:
    sal_bonus = sal_bonus + 500
if vendas > 5000 and vendas <= 7500:
    sal_bonus = sal_bonus + 700
if vendas >= 7500:
    sal_bonus = sal_bonus + 1000

sal_total = sal_fixo + sal_bonus

print('O salário final é', sal_total, 'e o bônus foi de', sal_bonus)