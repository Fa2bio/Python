__author__ = 'Fabio'
import random
import pickle

def cria_nome():
        return nomes[random.randint(0, 19)] + " " + sobrenomes[random.randint(0, 19)]


def cria_arquivo(n):
    pessoa = open("Lista de pessoas_2.txt", "wb")
    for i in range(n):
        pickle.dump(cria_nome(), pessoa)
        pickle.dump(random.randint(1, 99), pessoa)
        pickle.dump(round(random.uniform(1, 2), 2), pessoa)
    pessoa.close()
nomes = ["Fabio", "Anderson", "Vitor", "Danilo", "Lisa", "Bart", "Homer", "Magie", "Burns", "Moe",
               "Marge", "Selma", "Patty", "Bender", "Naruto", "Sasuke", "Sakura", "Peter",
               "Debora", "Goku"]
sobrenomes = ["Simpson", "Silva", "Scotelaro", "Mota", "Rafarillo", "Correa", "Sandes", "Sander", "",
                    "Anaraue", "Most", "Cube", "Carvalho", "Grey", "kalifa", "Ann",
                    "Akira", "Ramalho", "Magul", "Fast"]
numero = eval(input("Digite o numero de pessoas: "))

cria_arquivo(numero)
