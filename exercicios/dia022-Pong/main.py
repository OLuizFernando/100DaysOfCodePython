from turtle import Screen
from time import sleep
from paddle import *
from ball import *

s = Screen()
s.bgcolor('black')
s.setup(width=900, height=600)
s.title('Pong')
s.tracer(0)
s.listen()

barra1 = Barra(x=-400)
barra2 = Barra(x=400)
bola = Bola()

s.onkeypress(key='w', fun=barra1.cima)
s.onkeypress(key='s', fun=barra1.baixo)
s.onkeypress(key='Up', fun=barra2.cima)
s.onkeypress(key='Down', fun=barra2.baixo)

for y in range(-300, 301, 20):
    ponto = Turtle(shape='square')
    ponto.color('white')
    ponto.shapesize(0.25, 0.25)
    ponto.penup()
    ponto.goto(x=0, y=y)

while True:
    s.update()
    bola.mover()
    sleep(0.025)

s.exitonclick()