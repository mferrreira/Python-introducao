import random



nove_digitos = ''
for i in range(0,9):
    nove_digitos += str(random.randint(0,9))

regressiva_digito1 = 10
regressiva_digito2 = 11

resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * regressiva_digito1
    regressiva_digito1 -= 1

digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

resultado_digito_2 = 0
dez_digitos = nove_digitos + str(digito_1)
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * regressiva_digito2
    regressiva_digito2 -= 1

digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

novo_cpf = f'{nove_digitos}{digito_1}{digito_2}'
print(novo_cpf)
