"""
Variáveis são usadas para salvar algo na memória do computador.
PEP8: inicie variáveis com letras minúsculas, pode user números
e underline(_)

O sinal de = é o operador de atribuição. Ele é usado para 
atribuir um valor a uma variável

Uso: nomeVariável = expressão
"""

nome_completo = 'Marcio Martins Ferreira'   # snake_case
somaDoisMaisDois = 2 + 2                    # camelCase

print(nome_completo,somaDoisMaisDois)

print(int('1'), type(int('1')))             # repetição de 'int('1')'

# para evitar repetição, atribui a expressão repetida a uma variável e a utiliza pelo código

int_um = bool('1')              
print(int_um, type(int_um))

# CleanCode: nomear variáveis de maneira descritiva. int != bool



nome = 'marcio'
idade = 21
maior_de_idade = idade >= 18

print('Nome: ', nome, 'Idade: ', idade)
print('É maior? ', maior_de_idade)