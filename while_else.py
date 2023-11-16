"""
while/else -> executa quando o while chega ao final de sua execução, 
mas não quando econtra um break
"""

string = 'valor qualquer'

i = 0
while i < len(string):
    letra = string[i]

    print(letra)
    i += 1
else:
    print('O else foi executado.')
print('Fora do while')