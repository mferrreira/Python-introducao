"""
Operadores lógicos

and (e) or (ou) not (não)

and: Todas as condições precisam ser verdadeiras
se qualquer valor for considerado falso, a 
expressão inteira será avaliada naquele valor

São considerados falsy:
0
0.0
''
False

Também existe o tipo None, que é usado para 
representar um não valor
"""

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('senha: ')

senha = '12345678'

if entrada == 'E' and senha_digitada == senha:
    print('entrou')
else:
    print('Sair')