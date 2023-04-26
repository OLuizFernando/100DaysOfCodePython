import random as rd

lista_palavras = ['python', 'desenvolvimento', 'computador', 'aprendizado', 'software', 'sistema', 'linguagem']
espacos = []
vidas = 6
palavra = rd.choice(lista_palavras)
for c in range(len(palavra)):
    espacos.append('_')
    print(espacos[c], end=' ')
print()
while vidas > 0 and '_' in espacos:
    chute = str(input('Digite uma letra: ')).lower().strip()[0]
    for c in range(len(palavra)):
        if chute == palavra[c]:
            espacos[c] = chute
        elif chute not in palavra:
            print(f'A letra "{chute}" não está na palavra.')
            vidas -= 1
            print(f'Agora você tem {vidas} vidas.')
            break
    if chute in palavra and '_' in espacos:
        for espaco in espacos:
            print(espaco, end=' ')
        print()
print(f'Você venceu! A palavra é {palavra}')