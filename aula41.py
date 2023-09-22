## Aprendendo While/Else
"""
Caso um break seja executado no código, o else não será executado.
O else apenas será executado quando o while é inteiramente executado.
"""
string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        break

    print(letra)
    i += 1
else:
    print('Não encontrei um espaço na string.')
print('Fora do while.')