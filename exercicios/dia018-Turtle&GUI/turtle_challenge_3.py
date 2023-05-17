from turtle import Turtle, Screen

t = Turtle()
t.shape('turtle')
t.speed('fastest')
s = Screen()
angulo = 3
t.penup()
t.left(90)
t.forward(400)
t.right(90)
t.pendown()
while True:
    for _ in range(angulo):
        t.right(360 / angulo)
        t.forward(50)
    angulo += 1