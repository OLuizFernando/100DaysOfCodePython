from turtle import Turtle, Screen

t = Turtle()
s = Screen()


def frente():
    t.forward(10)


def tras():
    t.backward(10)


def direita():
    t.right(10)


def esquerda():
    t.left(10)


s.listen()
s.onkey(key='w', fun=frente)
s.onkey(key='a', fun=esquerda)
s.onkey(key='s', fun=tras)
s.onkey(key='d', fun=direita)
s.exitonclick()