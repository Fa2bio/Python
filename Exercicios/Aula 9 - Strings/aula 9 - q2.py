__author__ = 'Fabio'
def manipu(dna):
    cadeia = "".maketrans("ACTG", "TGAC")
    return dna.translate(cadeia)

dna = input('Digite a cadeia: ')
print(manipu(dna))