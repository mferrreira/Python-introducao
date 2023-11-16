"""
desempatocamento - quase igual o destructuring do js,
mas o resto deve ser tratado, nomalmente com '_'
"""

nome1, *_ = ['Marcio', 'flávia', 'chico']
_, nome2, *_ = ['Marcio', 'flávia', 'chico']

print(nome1)
print(nome2)
