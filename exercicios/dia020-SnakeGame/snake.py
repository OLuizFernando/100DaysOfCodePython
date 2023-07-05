from turtle import Turtle


class Cobra:

    def __init__(self):
        self.corpo = []
        self.criar_cobra()
        self.cabeca = self.corpo[0]

        # Cria a cobra, segmento por segmento e os coloca na posição inicial
    def criar_cobra(self):
        for pos in range(0, -101, -20):
            segmento = Turtle('square')
            segmento.color('#2C301D')
            segmento.penup()
            segmento.goto(x=pos, y=0)
            self.corpo.append(segmento)

    def mover(self):
        # faz a cobra se mover constantemente
        for segmento in range(len(self.corpo) - 1, 0, -1):
            # os segmentos do corpo acompanham o da cabeça
            self.corpo[segmento].goto(x=self.corpo[segmento - 1].xcor(), y=self.corpo[segmento - 1].ycor())
        self.cabeca.forward(20)

    # Define cada função para direcionar a cabeça da cobra
    def cima(self):
        self.cabeca.setheading(90)

    def esquerda(self):
        self.cabeca.setheading(180)

    def baixo(self):
        self.cabeca.setheading(270)

    def direita(self):
        self.cabeca.setheading(0)