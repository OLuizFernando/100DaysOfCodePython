from turtle import Screen, Turtle
from time import sleep

# configura a janela
s = Screen()
s.setup(width=600, height=600)
s.bgcolor('#8DA259')
s.title('Jogo da Cobrinha')
# desliga o tracer para permitir a atualização manual dos frames
s.tracer(0)

# constrói a cobra por segmentos e coloca na posição inicial
cobra = []
for pos in range(0, -101, -20):
    corpo = Turtle('square')
    corpo.color('#2C301D')
    corpo.penup()
    corpo.goto(x=pos, y=0)
    cobra.append(corpo)

# funções que fazem a cobra se mover
def cima():
    cobra[0].setheading(90)


def baixo():
    cobra[0].setheading(270)


def esquerda():
    cobra[0].setheading(180)


def direita():
    cobra[0].setheading(0)


while True:
    # update manual dos frames
    s.update()
    sleep(0.1)
    # faz a cobra andar, segmento por segmento
    for corpo in range(len(cobra) - 1, 0, -1):
        cobra[corpo].goto(x=cobra[corpo - 1].xcor(), y=cobra[corpo - 1].ycor())
    cobra[0].forward(20)
    s.listen()
    s.onkey(key='w', fun=cima)
    s.onkey(key='a', fun=esquerda)
    s.onkey(key='s', fun=baixo)
    s.onkey(key='d', fun=direita)


s.exitonclick()