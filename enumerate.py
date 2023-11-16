"""
Enumerate - enumera iteráveis (índices)
"""

lista = ['marcio','kim','gui']
lista.append('mauro')

lista_enumerada = enumerate(lista)
# print(list(lista_enumerada))     consumiu o iterador

for nome in lista_enumerada:
    print(nome)
# Iterator consumido, não há mais valores para serem retornados

for item in lista_enumerada:
    print(item) # nada 

# desempacotamento:

for indice, nome in enumerate(lista):
    print(indice, nome)