"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

cpf = input('Digite um CPF: ').replace('.','').replace('-','').strip()
num_multi = 10
lista_multiplicacoes = []
soma = 0
if len(cpf) == 11:
    for numero in cpf[:9]:
        lista_multiplicacoes.append(int(numero) * num_multi)
        num_multi -= 1

    for item in lista_multiplicacoes:
        soma += item
    
    multiplicacao = soma * 10
    resto = multiplicacao % 11
    if resto > 9:
        primeiro_digito = 0
    else:
        primeiro_digito = resto
    
    num_multi = 11
    lista_multiplicacoes = []
    soma = 0
    for numero in cpf[:10]:
        lista_multiplicacoes.append(int(numero) * num_multi)
        num_multi -= 1

    for item in lista_multiplicacoes:
        soma += item
    multiplicacao = soma * 10
    resto = multiplicacao % 11
    if resto > 9:
        segundo_digito = 0
    else:
        segundo_digito = resto

    if int(cpf[9]) == primeiro_digito and int(cpf[10]) == segundo_digito:
        print('CPF válido')
    else:
        print('CPF inválido')
    
    
else:
    print('O CPF informado não contém 11 dígitos.')