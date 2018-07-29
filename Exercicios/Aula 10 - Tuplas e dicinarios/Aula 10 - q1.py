__author__ = 'Fabio'
def ler_texto(x):
    vogais = {}
    if 'a' in x:
        vogais['a'] = [x.count("a")]
    if 'e' in x:
        vogais['e'] = [x.count("e")]
    if 'i' in x:
        vogais['i'] = [x.count("i")]
    if 'o' in x:
        vogais['o'] = [x.count("o")]
    if 'u' in x:
        vogais['u'] = [x.count("u")]
    return vogais

texto = input("Digite o texto a ser lido: ").lower()
print(ler_texto(texto))
