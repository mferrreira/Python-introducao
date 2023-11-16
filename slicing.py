"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321

Fatiamento [inicio:fim:passo] [::]

Obs.: a função len retorna qtd
de caracteres da str
"""

variavel = 'Olá mundo'
print(variavel[4:])
print(variavel[:4])
print(variavel[0:9:2])
print(variavel[::-1])