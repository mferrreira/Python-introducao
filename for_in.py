texto = 'Python'

for letra in texto:
    print(letra)

"""
For + Range
range -> range(start, stop, step)
"""

numeros = range(0, 10, 2)

for numero in numeros:
    print(numero)


"""
Iterável -> str, range, etc (__iter__())
Iterador -> quem sabe entregar um valor por vez

next ->  me entregue o próximo valor
iter -> me entregue seu iterador
"""

texto = iter('Marcio')  # __iter__()

print(next(texto))
print(next(texto))
print(next(texto))
print(next(texto))
print(next(texto))
print(next(texto))
print(next(texto)) # Erro StopIteration para a iteração



# For por baixo dos panos

texto2 = 'Marcio'
iterador = iter(texto)

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:       # trata apenas esse erro
        break
