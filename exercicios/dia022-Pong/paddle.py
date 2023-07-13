from turtle import Turtle


class Barra(Turtle):

    def __init__(self, x):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.setheading(90)
        self.shapesize(1, 5)
        self.penup()
        self.goto(x=x, y=0)

    def cima(self):
        if self.ycor() < 240:
            self.forward(20)

    def baixo(self):
        if self.ycor() > -240:
            self.backward(20)