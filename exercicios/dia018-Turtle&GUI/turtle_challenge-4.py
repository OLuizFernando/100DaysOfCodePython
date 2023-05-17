from turtle import Turtle, Screen
from random import choice, randint

t = Turtle()
cores = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
# direcoes = [0, 90, 180, 270]
t.pensize(2.5)
t.speed('fastest')
while True:
    t.color(choice(cores))
    t.forward(10)
    # t.setheading(choice(direcoes))
    t.setheading(randint(0, 359))