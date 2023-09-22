## Exercício

"""
Retorne qual letra apareceu mais vezes na frase.
"""
frase = 'O Python é uma linguagem de programação multiparadigma.'\
        'Python foi criado por Guido van Rossum.'.lower()
i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''
while i < len(frase):
    letra_atual = frase[i]
    qtd_usada = frase.count(letra_atual)
    i += 1

    if letra_atual == ' ':
        continue

    print(f'A letra {letra_atual} foi usada {qtd_usada} vezes.')

    if qtd_usada > qtd_apareceu_mais_vezes:
        qtd_apareceu_mais_vezes = qtd_usada
        letra_apareceu_mais_vezes = letra_atual

print(f'A letra que mais apareceu na frase foi a letra "{letra_apareceu_mais_vezes}", sendo utilizada {qtd_apareceu_mais_vezes} vezes.')
    