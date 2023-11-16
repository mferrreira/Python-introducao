"""
Repetições
while (enquanto)

Executa uma ação enquanto uma condição for verdadeira
"""

condicao = True

while condicao:
    nome = input('Qual o seu nome: ')
    print(f'seu nome é {nome}')

    if nome == 'sair':
        break # sai do while mais próximo

print('acabou')