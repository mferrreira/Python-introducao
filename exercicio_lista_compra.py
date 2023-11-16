"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de 
inserir, apagar e listar valores da sua lista

não permita que o programa quebre com 
erros de índices inexistentes na lista
"""

compras = []

while True:
    opcao = input('[i]nserir, [a]pagar, [l]istar, [s]air: \n').lower()
    indices_compras = range(len(compras))

    if opcao.startswith('s'):
        break

    elif opcao.startswith('i'):
        novo_item = input('Digite o item que deseja adicionar: ')
        compras.append(novo_item)

    elif opcao.startswith('a'):
        opcao_apagar = int(input('Digite o índice que deseja apagar: '))

        if opcao_apagar in indices_compras:
            del compras[opcao_apagar]
            continue
        else:
            print('não foi possível apagar esse índice')
            continue

    elif opcao.startswith('l'):
        if compras:
            for i, item in enumerate(compras):
                print(i, item)
            continue
        else:
            print('lista vazia!')
            continue
    else:
        print('Opção inválida!')
        continue