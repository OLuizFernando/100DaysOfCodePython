from turtle import Turtle


class Placar(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color('#2C301D')
        self.pontuacao = 0
        self.escrever()

    def escrever(self):
        self.goto(0, 270)
        self.write(arg=f'Pontuação: {self.pontuacao}', move=True, align='center', font=('Small Fonts', 15, 'bold'))

    def game_over(self):
        self.goto(0, -25)
        self.write(arg=f'GAME OVER', move=True, align='center', font=('Small Fonts', 50, 'bold'))