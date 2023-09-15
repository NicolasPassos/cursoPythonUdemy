nome = 'Nicolas'
altura = 1.67
peso = 67
imc = peso/(altura**2)

"f-strings"

linha_1 = f'{nome} tem {altura} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}' #Forçando a quantidade de casas decimais

print(linha_1)
print(linha_2)
print(linha_3)