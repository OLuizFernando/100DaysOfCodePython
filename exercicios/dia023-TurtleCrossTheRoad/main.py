from turtle import Screen
from time import sleep
from player import *
from cars import *
from scoreboard import *

s = Screen()
s.tracer(0)
s.bgcolor('#444444')
s.setup(width=900, height=900)
s.title('Turtle Cross The Road')
s.listen()

for x in range(-450, 451, 80):
    ponto = Turtle(shape='square')
    ponto.color('yellow')
    ponto.shapesize(0.5, 1)
    ponto.penup()
    ponto.goto(x=x, y=10)

tartaruga = Tartaruga()
gerenciador_carros = GerenciadorCarros()
placar = Placar()

s.onkey(key='w', fun=tartaruga.andar)
s.onkey(key='Up', fun=tartaruga.andar)

nivel = 1

rodando = True
while rodando:

    placar.escrever(f'Nível: {nivel}')
    sleep(0.025)
    s.update()

    gerenciador_carros.criar_carro_dir(nivel)
    gerenciador_carros.criar_carro_esq(nivel)
    gerenciador_carros.mover_carros(nivel)
    gerenciador_carros.limpar()

    if tartaruga.ycor() < 10:
        for carro in gerenciador_carros.carros_dir:
            if tartaruga.distance(carro) < 40:
                s.update()
                placar.game_over()
                rodando = False

    if tartaruga.ycor() > 10:
        for carro in gerenciador_carros.carros_esq:
            if tartaruga.distance(carro) < 40:
                s.update()
                placar.game_over()
                rodando = False

    if tartaruga.ycor() >= 425:
        s.update()
        tartaruga.goto(x=0, y=-400)
        nivel += 1
        placar.clear()

s.exitonclick()