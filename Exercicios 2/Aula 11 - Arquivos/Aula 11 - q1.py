__author__ = 'Fabio'
import random
def nome():
        return nomes[random.randint(0, 19)] + " " + sobrenomes[random.randint(0, 19)]


def cria_arquivo(n):
    pessoa = open("Lista de pessoas.txt", "w")
    for i in range(n):
        pessoa.write(str(nome()) + " " + str(random.randint(1, 99)) + str("\n"))
    pessoa.close()
nomes = ["Fabio", "Anderson", "Vitor", "Danilo", "Lisa", "Bart", "Homer", "Magie", "Burns", "Moe",
               "Marge", "Selma", "Patty", "Bender", "Naruto", "Sasuke", "Sakura", "Peter",
               "Debora", "Goku"]
sobrenomes = ["Simpson", "Silva", "Scotelaro", "Mota", "Rafarillo", "Correa", "Sandes", "Sander", "",
                    "Anaraue", "Most", "Cube", "Carvalho", "Grey", "kalifa", "Ann",
                    "Akira", "Ramalho", "Magul", "Fast"]
numero = eval(input("Digite o numero de pessoas: "))

cria_arquivo(numero)
