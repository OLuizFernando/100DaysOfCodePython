from turtle import Screen, Turtle
from paddles import *

s = Screen()
s.bgcolor('black')
s.setup(width=900, height=600)
s.title('Pong')
s.listen()

barra1 = Barra1()
barra2 = Barra2()

s.onkeypress(key='w', fun=barra1.cima)
s.onkeypress(key='s', fun=barra1.baixo)
s.onkeypress(key='Up', fun=barra2.cima)
s.onkeypress(key='Down', fun=barra2.baixo)

for y in range(-300, 301, 20):
    ponto = Turtle(shape='square', visible=False)
    ponto.color('white')
    ponto.shapesize(0.25, 0.25)
    ponto.penup()
    ponto.speed('fastest')
    ponto.goto(x=0, y=y)
    ponto.showturtle()

s.exitonclick()