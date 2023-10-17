# Criando um gerador de CPFs

import random

cpf = ''
lista_multiplicacoes = []
num_multi = 10
soma = 0

for i in range(9):
    cpf += str(random.randint(0,9))

for numero in cpf:
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

for numero in cpf:
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

cpf_gerado = cpf+str(primeiro_digito)+str(segundo_digito)

print(f'CPF gerado: {cpf_gerado}')