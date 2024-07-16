import random
palavras = ['openai', 'programador', 'ti', 'data drive', 'python']

palavra = random.choice(palavras)
letras_corretas = []
letras_erradas = []
tentativas = 6

while True:
    palavra_secreta = ''
    for letra in palavra:
        if letra in letras_corretas:
            palavra_secreta += letra
        else:
            palavra_secreta += '_'

    print('Palavra:', palavra_secreta)
    print('Letras erradas:', letras_erradas)
    print('Tentativas restantes:', tentativas)

    if palavra_secreta == palavra:
        print('Parabéns! Você venceu')
        break

    elif tentativas == 0:
        print('Você perdeu! A palavra era:', palavra)
        break

    letra_usuario = input('Digite uma letra: ').lower()

    if letra_usuario in palavra:
        print('Letra correta!')
        letras_corretas.append(letra_usuario)
    else:
        print('Letra errada!')
        letras_erradas.append(letra_usuario)
        tentativas -=1