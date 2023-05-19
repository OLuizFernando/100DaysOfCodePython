from turtle import Turtle, exitonclick
from random import randint

# declaração de variáveis e cores das tartarugas
vermelho = Turtle()
vermelho.color('red')
amarelo = Turtle()
amarelo.color('yellow')
verde = Turtle()
verde.color('lime green')
azul = Turtle()
azul.color('blue')
roxo = Turtle()
roxo.color('dark orchid')

tartarugas = [roxo, azul, verde, amarelo, vermelho]

# setando a posição inicial, formato e tamanho das tartarugas
posicao = 0
for tartaruga in tartarugas:
    tartaruga.shape('turtle')
    tartaruga.shapesize(2)
    tartaruga.penup()
    tartaruga.setposition(-400, -200 + posicao)
    posicao += 100



exitonclick()