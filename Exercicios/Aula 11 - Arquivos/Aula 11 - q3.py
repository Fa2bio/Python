__author__ = 'Fabio'
def arquivo(a, b):
    arquivo_1 = open(a, "r")
    arquivo_2 = open(b, 'w')
    loop = True
    while loop is True:
        linha = arquivo_1.readline()
        if linha == "":
            loop = False
        elif linha[0] != "/" and linha[1] != "/":
            arquivo_2.write(linha)
    arquivo_1.close()
    arquivo_2.close()
arquivo("arquivo_original.txt", "arquivo_modificado.txt")