"iterando string com while"

nome = 'Márcio Ferreira'
novo_nome = ''

i = 0
while i < len(nome):
    letra = nome[i]
    novo_nome += f'*{letra}'
    i += 1

print(novo_nome)