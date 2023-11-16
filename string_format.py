# formatação de Strings

nome = 'marcio'
altura = 1.66
peso = 54
imc = peso / (altura) ** 2

# Adicionando 'f' ao começo da string, ativa-se a formatação f-string

linha1 = f'{nome} tem {altura} de altura,'
linha2 = f'pesa {peso} quilos e seu imc é {imc}'

print(linha1)
print(linha2)