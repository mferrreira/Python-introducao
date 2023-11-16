a = 'A'
b = 'B'
c = 1.1
string1 = 'a={} b={} c={}'
string2 = 'a={0} b={0} c={1} d={2}' # suporta indexação
formato = string1.format(a,b,c)
formato = string2.format(a,b,c)

print(formato)


# o método format adiciona os argumentos passados aos campos entre chaves da string