"""
Conversão de tipos, coerção, type convertion, 
typecasting, coercion, é o ato de converter 
um tipo em outro.

Tipos imutáveis e primitivos:
str, int, float, bool
"""

print(1 + 1)                        # soma 1+1      = 2
print('a' + 'b')                    # concatena a+b = ab

# Usar a mesma expressão ('+') para tipos diferentes é o conceito de polimorfismo na programação

# print('1' + 1)       retorna erro

print(int('1'), type(int('1')))
print(int('1') + 1)                 # coerção
print(bool(''))                     # False
print(bool(' '))                    # True

print(str(11) + 'b')                # coerção


'''
int()
float()
bool()
str()
'''