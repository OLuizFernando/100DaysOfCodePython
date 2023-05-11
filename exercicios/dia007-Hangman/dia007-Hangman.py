# Melhor experiência ao executar no terminal do windows
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
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lista_palavras = ['executar', 'computador', 'programa', 'sistema', 'linguagem', 'aprender', 'jogo', 'forca', 'projeto',
                  'aula', 'carro', 'batata', 'tela', 'pedra', 'cabo', 'mesa', 'tecnologia', 'hora', 'teclado', 'amor',
                  'cachorro', 'brasil', 'mar', 'tropical', 'casa', 'livro', 'cadeira', 'zumbi', 'filme', 'arte']
while True:
    palavra = rd.choice(lista_palavras)
    espacos = []
    repetidas = []
    vidas = 6

    os.system('cls')
    for c in range(len(palavra)):
        espacos.append('_')
        print(espacos[c], end=' ')
    print()
    while vidas > 0 and '_' in espacos:
        while True:
            print(forcas[vidas])
            chute = str(input('Digite uma letra: ')).lower().strip()[0]
            os.system('cls')
            if chute in 'áàãâäéèêëíìîïóòõôöúùûüç':
                print(f'\033[31mERRO: Letras com acentos não são válidas.\033[m\n')
                for espaco in espacos:
                    print(espaco, end=' ')
                print()
            elif chute in repetidas:
                print(f'\033[31mERRO: A letra {chute} já foi digitada. Tente outra letra.\033[m\n')
                for espaco in espacos:
                    print(espaco, end=' ')
                print()
            elif chute.isalpha():
                repetidas.append(chute)
                break
            else:
                print(f'\033[31mERRO: "{chute}" não é um chute válido. Tente uma letra.\033[m\n')
                for espaco in espacos:
                    print(espaco, end=' ')
                print()
        for c in range(len(palavra)):
            if chute == palavra[c]:
                espacos[c] = chute
            elif chute not in palavra:
                vidas -= 1
                print(f'A letra "{chute}" não está na palavra.')
                print(f'Agora você tem \033[31m{vidas}\033[m vidas.')
                print()
                break
        if '_' in espacos and vidas > 0:
            for espaco in espacos:
                print(espaco, end=' ')
            print()
    print(forcas[vidas])
    if vidas > 0:
        print(f'\033[32mVocê venceu! A palavra é "{palavra}".\033[m')
    else:
        print(f'\033[31mVocê perdeu! A palavra era "{palavra}".\033[m')
    continuar = str(input('\nQuer jogar mais uma vez? [S/N] ')).strip().lower()[0]
    if continuar == 'n':
        break