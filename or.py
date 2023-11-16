entrada = input("[E]ntrar [S]air")
senha_digitada = input('Senha: ')

senhna_permitida = '12345678'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senhna_permitida:
        print('entrar')
if entrada == 'S' or entrada == 's':
        print('sair')

# Avaliação de curto circuito

senha = input('Senha: ') or 'Sem senha'

if not senha:
    print('Senha incorreta')