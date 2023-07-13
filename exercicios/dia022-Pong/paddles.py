from turtle import Turtle


class Barra1(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape('square')
        self.color('white')
        self.setheading(90)
        self.shapesize(1, 4)
        self.penup()
        self.speed('fastest')
        self.goto(x=-400, y=0)
        self.showturtle()

    def cima(self):
        if self.position() != (-400, 260):
            self.forward(20)

    def baixo(self):
        if self.position() != (-400, -260):
            self.backward(20)


class Barra2(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape('square')
        self.color('white')
        self.setheading(90)
        self.shapesize(1, 4)
        self.penup()
        self.speed('fastest')
        self.goto(x=400, y=0)
        self.showturtle()

    def cima(self):
        if self.position() != (400, 260):
            self.forward(20)

    def baixo(self):
        if self.position() != (400, -260):
            self.backward(20)