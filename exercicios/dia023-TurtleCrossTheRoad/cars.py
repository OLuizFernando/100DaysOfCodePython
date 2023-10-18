from turtle import Turtle
from random import choice
from time import sleep

CORES = ['blue', 'yellow', 'red', 'blueviolet', 'magenta', 'orange']
POSICOES_DIR = [-290, -215, -140, -65]
POSICOES_ESQ = [85, 160, 235, 310]


class CarroDir(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(3, 5)
        self.color(choice(CORES))
        self.setheading(180)
        self.penup()
        self.goto(x=500, y=choice(POSICOES_DIR))

    def andar(self, velocidade):
        self.forward(velocidade)

    def resetar(self):
        self.__init__()


class CarroEsq(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(3, 5)
        self.color(choice(CORES))
        self.setheading(0)
        self.penup()
        self.goto(x=-500, y=choice(POSICOES_ESQ))

    def andar(self, velocidade):
        self.forward(velocidade)

    def resetar(self):
        self.__init__()
