##Exercícios

"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
palavra_secreta = 'antedeguemon'.lower()
tentativas = 0
letras_acertadas = ''

print('Advinhe a palavra secreta.')
while True:
    print(f'Você já tentou {tentativas}x')
    print('')
    letra_palpite = input('Digite uma letra: ').lower()
    
    if len(letra_palpite) > 1:
        print('Só é permitido uma letra por vez.')
        continue

    if letra_palpite in palavra_secreta:
        print(f'A letra {letra_palpite} está na palavra secreta!')
        print('')
        letras_acertadas += letra_palpite
        
        palavra_formada = ''
        for letra in palavra_secreta:
            if letra in letras_acertadas:
                palavra_formada += letra
            else:
                palavra_formada += '*'
    else:
        print(f'A letra {letra_palpite} não se encontra na palavra secreta.')

    print(palavra_formada)
    print('')

    if '*' not in palavra_formada:
        print('----------------------')
        print('Parabens, você ganhou!')
        print('----------------------')
        break

    tentativas += 1