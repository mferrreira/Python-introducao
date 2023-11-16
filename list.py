"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - Índices e fatiamento
Métodos úteis: 

    append,     - Adiciona um item ao final
    insert,     - Adiciona um item no índice escolhido
    pop,        - Remove e retorna do final ou índice escolhido
    del,        - Apaga um índice
    clear,      - Limpa a lista
    extend,     - Estende a lista
    +           - Concatena listas

Create, Read, Update, Delete (CRUD)
"""

#            01234
#           -54321
string =    'ABCDE'

# lista = list()
lista = [123, True, 'Márcio Ferreira', 1.2, []]                  # ''
lista[2] = 'Flávia'         # MUTÁVEL
print(lista, type(lista))


outra_lista = [10,20,30,40]
numero = outra_lista[2] # 30
outra_lista[2] = 300
print(numero)

# deletar e reindexar lista
del outra_lista[2]

# adiciona ao final da lista
outra_lista.append(50)
outra_lista.append(60)
outra_lista.append(70)

print(outra_lista)

# remove e retorna o item da lista, argumento = indice
outra_lista.pop()
outra_lista.pop(3)

print(outra_lista)

# resetar lista
lista.clear()
print(lista)

lista.append(1)
lista.append(2)
lista.append('3')
lista.insert(1, 'oi')

print(lista)

# concatenação 

lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = lista_a + lista_b # concatena e retorna
lista_a.extend(lista_b)     # adiciona lista_b ao final de lista_a

print(lista_c)
print(lista_a)