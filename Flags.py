"""
Flag(bandeira) - marcar um local
None = não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""

condicao = True
passou_no_if = None     # flag

if condicao:
    passou_no_if = True
    print('faça algo')
else:
    print('Não faça algo')

print(passou_no_if, passou_no_if is None)