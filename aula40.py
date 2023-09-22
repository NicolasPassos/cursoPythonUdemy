## Criando uma calculadora
""" Calculadora com while """
while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite um operador (+ - / *): ')

    numeros_validos = None
    num1 = 0
    num2 = 0

    try:
        num1 = float(numero_1)
        num2 = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue
    
    operadores_permitidos = '+=/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue


    if operador == '+':
        print(num1 + num2)
    elif operador == '-':
        print(num1 - num2)
    elif operador == '/':
        print(num1 / num2)
    elif operador == '*':
        print(num1 * num2)
    else:
        print('Erro despecebido, informe ao dev.')
    

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break