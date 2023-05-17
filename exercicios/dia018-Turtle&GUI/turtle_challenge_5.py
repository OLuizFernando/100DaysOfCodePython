from turtle import Turtle, Screen

t = Turtle()
t.speed('fastest')
s = Screen()
cores = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
cor = 0
for angulo in range(0, 361, 5):
    t.color(cores[cor])
    if cor < 5:
        cor += 1
    else:
        cor = 0
    t.circle(200)
    t.setheading(angulo)
s.exitonclick()