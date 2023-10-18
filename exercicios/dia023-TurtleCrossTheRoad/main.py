from turtle import Screen, Turtle
from player import *
from cars import *

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
carro_dir = CarroDir()
carro_esq = CarroEsq()

s.onkey(key='w', fun=tartaruga.andar)
s.onkey(key='Up', fun=tartaruga.andar)

while True:

    s.update()

    carro_dir.andar(5)
    carro_esq.andar(5)

    sleep(0.025)

    if tartaruga.distance(carro_dir) < 65 or tartaruga.distance(carro_esq) < 65:
        break

    if tartaruga.ycor() >= 425:
        break

    if carro_dir.xcor() < -500:
        carro_dir.resetar()

    if carro_esq.xcor() > 500:
        carro_esq.resetar()

s.exitonclick()