from turtle import Turtle
from random import choice
from time import sleep

cores = ['blue', 'yellow', 'red', 'blueviolet', 'magenta', 'orange']
posicoes_dir = [-290, -215, -140, -65]
posicoes_esq = [85, 160, 235, 310]


class CarroDir(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(3, 5)
        self.color(choice(cores))
        self.setheading(180)
        self.penup()
        self.goto(x=500, y=choice(posicoes_dir))

    def andar(self, velocidade):
        self.forward(velocidade/5)

    def resetar(self):
        self.__init__()


class CarroEsq(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(3, 5)
        self.color(choice(cores))
        self.setheading(0)
        self.penup()
        self.goto(x=-500, y=choice(posicoes_esq))

    def andar(self, velocidade):
        self.forward(velocidade/5)

    def resetar(self):
        self.__init__()
