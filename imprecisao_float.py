"""
Imprecisão de ponto flutuante
"""
import decimal

numero1 = 0.1
numero2 = 0.7
numero_3 = numero1 + numero2

numero_4 = decimal.Decimal('0.1')
numero_5 = decimal.Decimal('0.7')
numero_6 = numero_4 + numero_5



print(numero_3)
print(f'{numero_3:.2f}')
print(round(numero_3, 2))

print(numero_6)
print(f'{numero_6:.2f}')
print(round(numero_6, 2))