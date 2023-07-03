from turtle import Screen, Turtle

s = Screen()
s.setup(width=600, height=600)
s.bgcolor('black')
s.title('Jogo da Cobrinha')
c001 = Turtle('square')
c002 = Turtle('square')
c003 = Turtle('square')
cobra = [c001, c002, c003]
pos = 0
for c in cobra:
    c.color('white')
    c.goto(x=pos, y=0)
    pos -= 20




s.exitonclick()