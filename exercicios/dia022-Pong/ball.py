from turtle import Turtle
from random import choice


class Bola(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.mover_x = choice([5, -5])
        self.mover_y = choice([5, -5])

    def mover(self):
        x = self.xcor() + self.mover_x
        y = self.ycor() + self.mover_y
        self.goto(x, y)

    def rebater(self):
        if 400 > self.xcor() > -400:
            self.mover_x *= -1

            if self.mover_x > 0:
                self.mover_x += 1

            if self.mover_x < 0:
                self.mover_x -= 1

    def quicar_y(self):
        self.mover_y *= -1
