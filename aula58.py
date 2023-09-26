## Exercício
'''
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de inserir, apagar e listar valores da lista
Não permita que o programa quebre com erros de indices inexistentes na lista
'''
lista_compras = []
while True:
    print('----------Lista de compras----------')
    print('')
    print('Selecione uma opção')
    acao = input('[i]nserir [a]pagar [l]istar: ').lower()

    if acao.startswith('i') == True:
        print('')
        item = input('Informe o item que deseja comprar: ').lower().capitalize()
        lista_compras.append(item)

    elif acao.startswith('a') == True:
        if len(lista_compras) == 0:
            print('Não há itens na lista.')
            continue
        elif len(lista_compras) == 1:
            print('A lista contém apenas um item.')
            apagar = input(f'Deseja apagar o item {lista_compras[0]}? [s]im [n]ão ').lower()
            if apagar.startswith('s'):
                lista_compras.pop(0)
            else:
                continue
        else:
            print('Sua lista contém os seguintes itens: ')
            for index, item in enumerate(lista_compras):
                print(f'{index} - {item};')
            indice = input('Informe o indice do item que será alterado: ')
            try:
                indice = int(indice)
                lista_compras.pop(indice)
                print('Item da lista apagado.')
            except IndexError:
                print('Esse indice não existe na lista.')
                continue
            except ValueError:
                print('O valor informado não corresponde a um indice da lista.')
                continue
            
    elif acao.startswith('l') == True:
        if len(lista_compras) >= 1:
            print('Segue os itens em sua lista de compras: ')
            for item in lista_compras:
                print(f'{item};')
        else:
            print('Não há itens na lista.')
    else:
        print('A opção selecionada não existe.')
        continue
    print('')
