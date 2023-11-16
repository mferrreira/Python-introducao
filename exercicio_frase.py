frase = 'O python é uma lingugaem de programação '\
        'multiparadigma. ' \
        'Python foi criado por Guido Van Rossum'

i = 0

maior_repeticao_qtd = 0
letra_mais_repetida = ''

while i < len(frase):
    letra_atual = frase[i]
    quantas_vezes_a_letra_apareceu = frase.count(letra_atual)

    if letra_atual == ' ':
        i += 1
        continue

    if quantas_vezes_a_letra_apareceu > maior_repeticao_qtd:
        maior_repeticao_qtd = quantas_vezes_a_letra_apareceu
        letra_mais_repetida = letra_atual

    i += 1

print(letra_mais_repetida, maior_repeticao_qtd)