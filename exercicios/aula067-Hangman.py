import os
import random as rd
forcas = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''',]
lista_palavras = ['executar', 'computador', 'programa', 'sistema', 'linguagem', 'aprender', 'jogo', 'forca', 'projeto',
                  'aula', 'carro', 'batata', 'tela', 'pedra', 'cabo', 'mesa', 'tecnologia', 'hora', 'teclado', 'amor',
                  'cachorro', 'brasil', 'mar', 'tropical', 'casa', 'livro', 'cadeira', 'zumbi', 'filme', 'arte']
palavra = rd.choice(lista_palavras)
espacos = []
repetidas = []
vidas = 6

for c in range(len(palavra)):
    espacos.append('_')
    print(espacos[c], end=' ')
print()
while vidas > 0 and '_' in espacos:
    while True:
        chute = str(input('Digite uma letra: ')).lower().strip()[0]
        os.system('cls')
        if chute in 'áàãâäéèêëíìîïóòõôöúùûüç':
            print(f'\033[31mERRO: Letras com acentos não são válidas.\033[m')
        elif chute in repetidas:
            print(f'\033[31mERRO: A letra {chute} já foi digitada. Tente outra letra.\033[m')
        elif chute.isalpha():
            repetidas.append(chute)
            break
        else:
            print(f'\033[31mERRO: "{chute}" não é um chute válido. Tente uma letra.\033[m')
    for c in range(len(palavra)):
        if chute == palavra[c]:
            espacos[c] = chute
        elif chute not in palavra:
            vidas -= 1
            print(forcas[vidas])
            print(f'A letra "{chute}" não está na palavra.')
            print(f'Agora você tem \033[31m{vidas}\033[m vidas.')
            break
    if '_' in espacos:
        for espaco in espacos:
            print(espaco, end=' ')
        print()
if vidas > 0:
    print(f'\033[32mVocê venceu! A palavra é "{palavra}".\033[m')
else:
    print(f'\033[31mVocê perdeu! A palavra era "{palavra}".\033[m')