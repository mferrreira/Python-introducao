"""
Operação ternária (condicional de uma linha)

<valor> if <condição> else <outro valor>

condicao = 10 == 11

variavel = 'Valor' if condicao else 'Outro valor'

"""

digito = 8

novo_digito  = digito if digito <= 9 else 0
novo_digito = 0 if digito > 9 else digito

