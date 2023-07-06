from turtle import Turtle


class Cobra:

    def __init__(self):
        self.corpo = []
        self.criar_cobra()
        self.cabeca = self.corpo[0]

        # cria a cobra, segmento por segmento e os coloca na posição inicial
    def criar_cobra(self):
        # cada segmento quadrado tem 20 x 20  de tamanho
        # a estrutura for irá criar 3 segmentos, 1° na posição 0, 2° na -20 e 3° na -40
        for pos in range(0, -41, -20):
            segmento = Turtle('square')
            segmento.color('#2C301D')
            segmento.penup()
            segmento.goto(x=pos, y=0)
            self.corpo.append(segmento)

    def novo_segmento(self):
        segmento = Turtle('square')
        segmento.color('#2C301D')
        segmento.penup()
        self.corpo.append(segmento)
        segmento.goto(x=self.corpo[0].xcor(), y=self.corpo[0].ycor())

    def mover(self):
        # faz a cobra se mover constantemente
        for segmento in range(len(self.corpo) - 1, 0, -1):
            # os segmentos de trás acompanham o segmento da frente (cabeça)
            self.corpo[segmento].goto(x=self.corpo[segmento - 1].xcor(), y=self.corpo[segmento - 1].ycor())
        self.cabeca.forward(20)

    # define cada função para direcionar a cabeça da cobra
    # só executa o comando se a direção da cobra não for a direção contrária, assim a cobra não dá ré
    def cima(self):

        if self.cabeca.heading() != 270:
            self.cabeca.setheading(90)

    def esquerda(self):
        if self.cabeca.heading() != 0:
            self.cabeca.setheading(180)

    def baixo(self):
        if self.cabeca.heading() != 90:
            self.cabeca.setheading(270)

    def direita(self):
        if self.cabeca.heading() != 180:
            self.cabeca.setheading(0)