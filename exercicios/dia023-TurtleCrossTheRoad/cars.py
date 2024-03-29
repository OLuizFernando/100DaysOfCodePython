from turtle import Turtle
from random import choice, randint

CORES = ['blue', 'yellow', 'red', 'blueviolet', 'magenta', 'orange', 'gray', 'white']
POSICOES_DIR = [-290, -215, -140, -65]
POSICOES_ESQ = [85, 160, 235, 310]


class GerenciadorCarros:

    def __init__(self):
        self.carros_dir = []
        self.carros_esq = []

    def criar_carro_dir(self, nivel):
        if nivel < 5:
            chance = randint(1, 8)
        else:
            chance = randint(1, 4)
        if chance == 1:
            novo_carro = Turtle('square')
            novo_carro.shapesize(2, 3)
            novo_carro.color(choice(CORES))
            novo_carro.setheading(180)
            novo_carro.penup()
            novo_carro.goto(x=500, y=choice(POSICOES_DIR))
            self.carros_dir.append(novo_carro)

    def criar_carro_esq(self, nivel):
        if nivel < 5:
            chance = randint(1, 8)
        else:
            chance = randint(1, 4)
        if chance == 1:
            novo_carro = Turtle('square')
            novo_carro.shapesize(2, 3)
            novo_carro.color(choice(CORES))
            novo_carro.setheading(0)
            novo_carro.penup()
            novo_carro.goto(x=-500, y=choice(POSICOES_ESQ))
            self.carros_esq.append(novo_carro)

    def mover_carros(self, passo):
        passo = passo * 2 + 3
        for i, carro in enumerate(self.carros_dir):
            if i == 0:
                carro.forward(passo)
            elif self.carros_dir[i - 1].xcor() < 425:
                carro.forward(passo)

        for i, carro in enumerate(self.carros_esq):
            if i == 0:
                carro.forward(passo)
            elif self.carros_esq[i - 1].xcor() > -425:
                carro.forward(passo)

    def limpar(self):
        for carro in self.carros_dir:
            if carro.xcor() < -500:
                carro.hideturtle()
                self.carros_dir.pop(0)
        for carro in self.carros_esq:
            if carro.xcor() > 500:
                carro.hideturtle()
                self.carros_esq.pop(0)
