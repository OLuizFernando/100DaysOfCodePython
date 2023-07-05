from turtle import Turtle


class Cobra:

    def __init__(self):
        self.corpo = []
        self.criar_cobra()

        # Cria a cobra, segmento por segmento e os coloca na posição inicial
    def criar_cobra(self):
        for pos in range(0, -101, -20):
            segmento = Turtle('square')
            segmento.color('#2C301D')
            segmento.penup()
            segmento.goto(x=pos, y=0)
            self.corpo.append(segmento)

    # Define cada função para direcionar a cabeça da cobra
    def cima(self):
        self.corpo[0].setheading(90)

    def esquerda(self):
        self.corpo[0].setheading(180)

    def baixo(self):
        self.corpo[0].setheading(270)

    def direita(self):
        self.corpo[0].setheading(0)