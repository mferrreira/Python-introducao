# input() coleta dados de entrada do usuário

nome = input('qual o seu nome? ')
print(f"o seu nome é {nome}")

numero1 = input('numero 1: ')
numero2 = input('numero 2: ')

# código concatena os números, input retorna tipo 'str'
resultado = numero1 + numero2
print(resultado)

# código agora soma mas quebra se digitar um caractere
numero_1 = int(input('outro numero 1: '))
numero_2 = int(input('outro numero 2: '))

print(numero_1 + numero_2)