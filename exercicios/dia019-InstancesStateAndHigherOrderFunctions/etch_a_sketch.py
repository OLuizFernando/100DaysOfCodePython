from turtle import Turtle, Screen

t = Turtle()
t.setheading(90)
s = Screen()


def frente():
    t.forward(10)


def tras():
    t.backward(10)


def direita():
    t.right(10)


def esquerda():
    t.left(10)


def reiniciar():
    t.reset()
    t.setheading(90)


s.listen()
s.onkeypress(key='w', fun=frente)
s.onkeypress(key='a', fun=esquerda)
s.onkeypress(key='s', fun=tras)
s.onkeypress(key='d', fun=direita)
s.onkeypress(key='c', fun=reiniciar)
s.exitonclick()