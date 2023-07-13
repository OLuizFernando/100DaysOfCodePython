from turtle import Turtle
from random import randint


class Bola(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()

    def mover(self):
        x = self.xcor() + 5
        y = self.ycor() + 5
        self.goto(x, y)