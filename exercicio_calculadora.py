"""Calculadora com While"""

while True:
    resultado = None

    num1 = input('Digite o primeiro número: ')
    num2 = input('Digite o segundo número: ')
    op =   input('Digite o operador: ') # * + - /

    numeros_validos = None

    try:
        num1_float = float(num1)
        num2_float = float(num2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Pelo menos um dos números digitados são inválidos')
        continue





    print(resultado)

    sair = input('quer sair? [s][n]: ').lower().startswith('s')
    if sair:
        break
    
