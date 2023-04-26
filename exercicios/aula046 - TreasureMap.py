linha1 = ['[ ]', '[ ]', '[ ]']
linha2 = ['[ ]', '[ ]', '[ ]']
linha3 = ['[ ]', '[ ]', '[ ]']
mapa = [linha1, linha2, linha3]
print(f'\033[34m1\033[m {linha1}\n\033[34m2\033[m {linha2}\n\033[34m3\033[m {linha3}')
print('-' * 25)
while True:
    posicao_linha = int(input('Em qual LINHA deseja colocar o tesouro? '))
    if 1 <= posicao_linha <= 3:
        break
    else:
        print('\033[31mERRO: Digite um número entre 1 e 3.\033[m')
print('\033[34m   1      2      3\033[m')
if posicao_linha == 1:
    print(f'\033[34m{linha1}\033[m\n{linha2}\n{linha3}')
elif posicao_linha == 2:
    print(f'{linha1}\n\033[34m{linha2}\033[m\n{linha3}')
else:
    print(f'{linha1}\n{linha2}\n\033[34m{linha3}\033[m')
print('-' * 25)
while True:
    posicao_coluna = int(input('Em qual COLUNA deseja colocar o tesouro? '))
    if 1 <= posicao_coluna <= 3:
        break
    else:
        print('\033[31mERRO: Digite um número entre 1 e 3.\033[m')
mapa[posicao_linha - 1][posicao_coluna - 1] = '[X]'
print('     1      2      3')
print(f'1 {linha1}\n2 {linha2}\n3 {linha3}')