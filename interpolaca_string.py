"""
Interpolação básica de strings

s       - string
d e i   - int
f       - float
x e X   - Hexadecimal
"""

nome = 'Marcio'
preco = 1000.9634891726
variavel  = '%s, o preço é R$%.2f' % (nome, preco) # parecido com C
print(variavel)

print('O hexadecimal de %d é %x' % (128, 128))