##Trabalhando com interpolação de strings
"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""
nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
#'%x' transforma o valor em hexadecimal e o '08' entre eles faz com que seja adicionado zeros a esquerda. 
print('O hexadecimal de %d é %08X' % (1500, 1500))