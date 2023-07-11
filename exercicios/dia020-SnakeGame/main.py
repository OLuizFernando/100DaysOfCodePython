from turtle import Screen
from time import sleep
from snake import *
from food import *
from scoreboard import *

# configura a janela
s = Screen()
s.setup(width=600, height=600)
s.bgcolor('#8DA259')
s.title('Jogo da Cobrinha')
s.listen()
# desliga o tracer para permitir a atualização manual dos frames
s.tracer(0)

cobra = Cobra()
comida = Comida()
placar = Placar()

while True:
    # update manual dos frames
    s.update()
    sleep(0.1)

    # faz a cobra se mover constantemente
    cobra.mover()

    # detecção das teclas para direcionar a cabeça da cobra
    s.onkeypress(key='w', fun=cobra.cima)
    s.onkeypress(key='Up', fun=cobra.cima)
    s.onkeypress(key='a', fun=cobra.esquerda)
    s.onkeypress(key='Left', fun=cobra.esquerda)
    s.onkeypress(key='s', fun=cobra.baixo)
    s.onkeypress(key='Down', fun=cobra.baixo)
    s.onkeypress(key='d', fun=cobra.direita)
    s.onkeypress(key='Right', fun=cobra.direita)

    # detecção de colisão com a comida
    if cobra.cabeca.distance(comida) < 10:
        comida.aparecer()
        cobra.novo_segmento()
        placar.clear()
        placar.pontuacao += 1
        placar.escrever()

    # detecção de colisão com a parede
    if cobra.cabeca.xcor() >= 300 or cobra.cabeca.xcor() <= -300 or cobra.cabeca.ycor() >= 300 or cobra.cabeca.ycor() <= -300:
        placar.game_over()
        break

s.exitonclick()