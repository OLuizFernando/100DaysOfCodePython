from turtle import Screen, Turtle
from time import sleep
from snake import *

# configura a janela
s = Screen()
s.setup(width=600, height=600)
s.bgcolor('#8DA259')
s.title('Jogo da Cobrinha')
# desliga o tracer para permitir a atualização manual dos frames
s.tracer(0)

# constrói a cobra por segmentos e coloca na posição inicial
cobra = Cobra()

while True:
    # update manual dos frames
    s.update()
    sleep(0.1)

    # faz a cobra se mover constantemente
    for segmento in range(len(cobra.corpo) - 1, 0, -1):
        # os segmentos do corpo acompanham o da cabeça
        cobra.corpo[segmento].goto(x=cobra.corpo[segmento - 1].xcor(), y=cobra.corpo[segmento - 1].ycor())
    cobra.corpo[0].forward(20)
    # detecção das teclas para direcionar a cabeça da cobra
    s.listen()
    s.onkeypress(key='w', fun=cobra.cima)
    s.onkeypress(key='a', fun=cobra.esquerda)
    s.onkeypress(key='s', fun=cobra.baixo)
    s.onkeypress(key='d', fun=cobra.direita)
    s.onkeypress(key='Up', fun=cobra.cima)
    s.onkeypress(key='Left', fun=cobra.esquerda)
    s.onkeypress(key='Down', fun=cobra.baixo)
    s.onkeypress(key='Right', fun=cobra.direita)

s.exitonclick()