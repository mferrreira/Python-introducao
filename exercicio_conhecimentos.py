"""
Excercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
SE nome e idade forem digitados:
    exiba:
        seu nome é: {nome}
        seu nome inverdido é: {nome invertido}
        seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        Seu nome contém espaços
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input('Digite o seu nome: ')
idade = input('Digite sua idade: ')

if not nome or not idade:
    print('Desculpe, você deixou campos vazios')
else:
    print(f'Seu nome é : {nome}')
    print(f'Seu nome invertido é: {nome[::-1]}')
    print(f'Seu nome tem {len(nome)} letras')
    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('seu nome não contém espaços')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
