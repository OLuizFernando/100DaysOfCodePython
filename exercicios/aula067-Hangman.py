import random as rd

lista_palavras = ['python', 'desenvolvimento', 'computador', 'aprendizado', 'software', 'sistema', 'linguagem']
espacos = []
vidas = 6
palavra = rd.choice(lista_palavras)
for letra in palavra:
    espacos.append('_')
for espaco in espacos:
    print(espaco, end=' ')
chute = str(input('\nDigite uma letra: ')).lower().strip()[0]
for c in range(0, len(palavra)):
    if chute == palavra[c]:
        espacos[c] = chute
    elif chute not in palavra:
        print(f'A letra "{chute}" não está na palavra.')
        vidas -= 1
        break
for espaco in espacos:
    print(espaco, end=' ')