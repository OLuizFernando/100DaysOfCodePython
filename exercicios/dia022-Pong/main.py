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

while True:
    barra_esq = Barra(x=-400)
    barra_dir = Barra(x=400)
    bola = Bola()

    s.onkeypress(key='w', fun=barra_esq.cima)
    s.onkeypress(key='s', fun=barra_esq.baixo)
    s.onkeypress(key='Up', fun=barra_dir.cima)
    s.onkeypress(key='Down', fun=barra_dir.baixo)

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

        if bola.ycor() > 290 or bola.ycor() < -280:
            bola.quicar_y()

        if bola.distance(barra_esq) <= 50 or bola.distance(barra_dir) <= 50:
            if bola.xcor() > 375 or bola.xcor() < -375:
                bola.quicar_x()

        if bola.xcor() > 430 or bola.xcor() < -440:
            break

    sleep(0.5)
    s.reset()

s.exitonclick()