"""
Split = divide uma string/list
join - une uma string/list
"""

frase = 'olha só que coisa daora'

lista_palavras = frase.split()

for i, frase in enumerate(lista_palavras):
    print(lista_palavras[i].strip())

print(lista_palavras)


frases_unidas = '-'.join('abc')

print(frases_unidas)