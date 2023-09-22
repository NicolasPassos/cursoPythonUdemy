##Exercícios
"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero_inteiro = input('Digite um número inteiro: ')
try:
    numero_inteiro = int(numero_inteiro)
    if numero_inteiro % 2 == 0:
        print(f'O número {numero_inteiro} é par.')
    else:
        print(f'O número {numero_inteiro} é impar.')
except:
    print('O valor digitado não é um número inteiro.')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
horario = input('Digite a hora atual: ')
try:
    horario = int(horario)
    if horario >= 0 and horario <= 11:
        print('Bão dia, meu nobre.')
    elif horario >= 12 and horario <=17:
        print('Boa tarde, meu nobre.')
    elif horario >= 18 and horario <= 23:
        print('Boa noite, meu nobre')
    else:
        print(f'Não existe a hora {horario}, meu nobre.')
except:
    print('A hora informada é inválida. Digite apenas a hora sem os minutos.')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('Digite seu primeiro nome: ')

if len(nome) <= 4:
    print('Seu nome é curto.')
elif len(nome) >= 5 and len(nome) <= 6:
    print('Seu nome é normal.')
else:
    print('Seu nome é muito grande.')