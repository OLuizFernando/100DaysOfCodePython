from turtle import Turtle
from random import randint


class Comida(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('#2C301D')
        self.speed('fastest')
        rand_x = randint(-285, 280)
        rand_y = randint(-280, 285)
        self.goto(rand_x, rand_y)

    def reaparecer(self):
        rand_x = randint(-285, 280)
        rand_y = randint(-280, 285)
        self.goto(rand_x, rand_y)