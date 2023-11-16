"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não
digite um número inteiro, informe que não é um número inteiro
"""

numero = input('Digite um número: ')

try:
    numero_int = int(numero)
    if numero_int % 2 == 0:
        print('é par')
    else:
        print('é ímpar')
except:
    print('Não é um número inteiro')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no 
horário descrito, exiba a saudação apropriada.
Ex: Bom dia: 0-11, Boa tarde 12-17 e Boa noite 18-23
"""

hora = input('Digite a hora (apenas a hora): ')
hora_int = int(hora)

if hora_int >= 0 and hora_int <= 11:
    print('Bom Dia!')
elif hora_int >= 12 and hora_int <= 17:
    print('boa tarde')
elif hora_int >= 18 and hora_int <= 23:
    print('Boa noite')
else:
    print('horário inválido')


"""
Faça um prorgama que peça o primeiro nome do usuário. Se o nome
tiver 4 letras ou menos escreva "seu nome é curto"; se tiver 
entre 5 e 6 letras, escreva "seu nome é normal"; maior que 6 
letras escreva "seu nome é muito grande"
"""

nome = input('Digite o seu primeiro nome: ')

if len(nome) <= 4:
    print('seu nome é curto')
elif len(nome) <= 6:
    print('seu nome é normal')
else:
    print('seu nome é grande')