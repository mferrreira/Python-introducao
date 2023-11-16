"""
Formatação básica de strings

s                               - string
d                               - int
f                               - float
.<número de dígitos>.f                           
x ou X                          - hexadecimal
(Caractere)(><^)(quantidade)    
>                               - esquerda
<                               - direita
^                               - centro
Sinal - + ou -                  
Ex.: 0>-100, .1f

!r !s !a                        - Conversion Flags
"""

variavel = 'abc'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
print(f'{1000.191287391839:,.1f}')
print(f'{variavel: ^10}')

print(f"O hexadecimal de 1500 é {1500:08X}")
print(f'{variavel!a}')