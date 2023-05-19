import time
from turtle import Turtle, Screen
from random import choice
from time import sleep

while True:
    # declaração de variáveis e cores das tartarugas
    s = Screen()
    s.title('CORRIDA DAS TARTARUGAS')
    s.setup(width=960, height=540)
    vermelho = Turtle()
    vermelho.nome = ['vermelho', 'vermelha']
    vermelho.color('red')
    amarelo = Turtle()
    amarelo.nome = ['amarelo', 'amarela']
    amarelo.color('yellow')
    verde = Turtle()
    verde.nome = 'verde'
    verde.color('lime green')
    azul = Turtle()
    azul.nome = 'azul'
    azul.color('blue')
    roxo = Turtle()
    roxo.nome = ['roxo', 'roxa', 'violeta']
    roxo.color('dark orchid')

    tartarugas = [roxo, azul, verde, amarelo, vermelho]
    cores = ['roxo', 'roxa', 'violeta', 'azul', 'verde', 'amarelo', 'amarela', 'vermelho', 'vermelha']

    # setando a posição inicial, formato, tamanho e passos das tartarugas
    posicao = 0
    for tartaruga in tartarugas:
        tartaruga.shape('turtle')
        tartaruga.shapesize(2)
        tartaruga.penup()
        tartaruga.setposition(x=-400, y=-200 + posicao)
        tartaruga.passos = 0
        posicao += 100

    # aposta do usuário
    while True:
        aposta = s.textinput('FAÇA SUA APOSTA', 'Em qual tartaruga você aposta? Escolha uma cor.').lower().strip()
        if aposta in cores:
            break

    # corrida sorteada
    while True:
        sleep(0.05)
        escolhida = choice(tartarugas)
        escolhida.forward(10)
        escolhida.passos += 10
        if escolhida.passos >= 840:
            vencedora = escolhida
            break

    if aposta in vencedora.nome:
        while True:
            jogar_novamente = s.textinput('RESULTADO', 'Você VENCEU!\nDeseja jogar novamente?').lower().strip()[0]
            if jogar_novamente in 'sn':
                break
        if jogar_novamente == 's':
            s.clear()
        else:
            break
    else:
        while True:
            jogar_novamente = s.textinput('RESULTADO', 'Você PERDEU!\nDeseja jogar novamente?').lower().strip()[0]
            if jogar_novamente in 'sn':
                break
        if jogar_novamente == 's':
            s.clear()
        else:
            break
