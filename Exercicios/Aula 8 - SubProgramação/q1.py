__author__ = 'Fabio'
def fatorial(n):
   if n <= 1:
      return 1
   else:
      return n*fatorial(n-1)
N = eval(input("digite o nº total de alunos: "))
M = eval(input("digite o nº de alunos do grupo M: "))
combinaçoes = fatorial(N)/(fatorial(M)*fatorial(N-M))
print('O número de combinações possíveis é:',combinaçoes)
