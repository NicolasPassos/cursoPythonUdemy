## Exercícios

"""
Iterando strings com while
Use o while para tratar uma string retornar um nome da seguinte maneira:
Ex: *N*i*c*o*l*a*s* *D*u*a*r*t*e
"""
nome = 'Nicolas Duarte'
contador = 0
nome_tratado = ''

while contador < len(nome):
    nome_tratado += f'*{nome[contador]}'
    contador += 1

print(nome_tratado)

