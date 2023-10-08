from turtle import Turtle


class Tartaruga(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('limegreen')
        self.shapesize(2, 2)
        self.setheading(90)
        self.penup()
        self.goto(x=0, y=-400)

    def andar(self):
        self.forward(25)