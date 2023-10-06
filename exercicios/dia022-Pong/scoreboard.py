from turtle import Turtle


class Placar(Turtle):

    def __init__(self, x, pontos):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x, 260)
        self.color('White')
        self.pontuacao = pontos
        self.escrever(x)

    def escrever(self, x):
        self.goto(x, 260)
        self.write(arg=self.pontuacao, move=True, align='center', font=('Small Fonts', 20))