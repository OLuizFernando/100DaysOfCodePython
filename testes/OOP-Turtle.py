from turtle import Turtle, Screen
tartaruga = Turtle()
print(tartaruga)
tartaruga.shape('turtle')
tartaruga.color('DarkOrchid1')
tela = Screen()
tela.bgcolor('black')
espiral = 0
tartaruga.setheading(90)
tartaruga.forward(100)
tela.exitonclick()