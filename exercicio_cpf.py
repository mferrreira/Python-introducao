"""
CPF: 119.220.206-64

Cálculo de 1 dígito do CPF

Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:    746.824.890-70
       
    10  9  8  7  6  5  4 3 2
*    7  4  6  8  2  4  8 9 0
    ___________________
    70 36 48 56 12 20 32 27 0

    
Somar todos os resultados:
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11

3010 % 11 = 7

Se o resultado anterior for maior que 9:
    resultado é 0
O contrário disso:
    restultado é o valor da conta

O primeiro dígito do CPF é 7
"""

cpf = input('Digite o CPF: ')

nove_digitos = cpf[:9]
dez_digitos = cpf[:10]
regressiva_digito1 = 10
regressiva_digito2 = 11

resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * regressiva_digito1
    regressiva_digito1 -= 1

digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * regressiva_digito2
    regressiva_digito2 -= 1

digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

novo_cpf = f'{nove_digitos}{digito_1}{digito_2}'
print(novo_cpf)

if novo_cpf == cpf:
    print(f'{cpf} válido')
else:
    print(f'cpf inválido')
