from turtle import Turtle


class Placar(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('White')

    def escrever(self, texto):
        self.goto(-390, 410)
        self.write(arg=texto, move=True, align='center', font=('Small Fonts', 20, 'bold'))

    def game_over(self):
        self.goto(0, -95)
        self.write(arg='GAME\nOVER', move=True, align='center', font=('Small Fonts', 115, 'bold'))