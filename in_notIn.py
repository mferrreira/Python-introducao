# Operadores in e not in 

# Strings são iteráveis

# 0 1 2 3 4 5
# M á r c i o 
#-6-5-4-3-2-1

nome = 'Marcio'
# print(nome[1])
# print(nome[-1])

print('a' in nome)
print('á' in nome)
print('Mar' in nome)
print(10 * '-')
print('z' not in nome)

nome = input('Digite o seu nome: ')
encontrar = input('Digite o que desenha encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em nome')