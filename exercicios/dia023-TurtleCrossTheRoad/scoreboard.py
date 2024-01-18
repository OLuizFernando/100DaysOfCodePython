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

    def ler_recorde(self):
        try:
            with open('recorde.txt', 'r') as arquivo:
                recorde = int(arquivo.read())
                return recorde
        except:
            return 0

    def atualizar_recorde(self, pontuacao):
        with open('recorde.txt', 'w') as arquivo:
            arquivo.write(str(pontuacao))

    def game_over(self, pontuacao, recorde):
        self.clear()
        self.goto(-450, 0)
        self.pendown()
        self.color('black')
        self.pensize(225)
        self.goto(450, 0)
        self.pensize(1)
        self.color('white')
        self.goto(0, -5)
        self.write(arg='GAME OVER', move=True, align='center', font=('Small Fonts', 115, 'bold'))
        self.goto(0, -45)
        self.write(arg=f'Pontuação: {pontuacao}', move=True, align='center', font=('Small Fonts', 20, 'bold'))
        self.goto(0, -85)
        self.write(arg=f'Recorde: {recorde}', move=True, align='center', font=('Small Fonts', 17, 'bold'))