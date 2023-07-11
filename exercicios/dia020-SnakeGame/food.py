from turtle import Turtle
from random import randint, choice

posicoes = [-280, -260, -240, -220, -200, -180, -160, -140, -120, -100, -80, -60, -40, -20, 0,
            20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280]

print(posicoes)

class Comida(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('#2C301D')
        self.speed('fastest')
        self.aparecer()

    def aparecer(self):
        rand_x = randint(-285, 280)
        rand_y = randint(-280, 285)
        self.goto(choice(posicoes), choice(posicoes))