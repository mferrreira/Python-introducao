"""
Condicional

if / elif / else


entrada = input('Você quer "entrar" ou "sair"?')

print('você entrou no sistema')
print('você saiu do sistema')

"""


entrada = input('"entrar" ou "sair"?')

if entrada == "entrar":
    print('entrou no sistema')
elif entrada == "sair":
    print('saiu do sistema')
else:
    print('voce não digitou nem entrar nem sair')

print('FORA DOS BLOCOS')