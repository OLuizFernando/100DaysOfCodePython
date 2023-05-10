from turtle import Turtle, Screen
# configurando a tartaruga
t = Turtle()
print(t)
t.shape('turtle')
t.color('DarkOrchid1')
t.pensize(5)

# configurando a tela
tela = Screen()
tela.bgcolor('black')


# posição inicial
t.penup()
t.left(90)
t.forward(100)
t.left(90)
t.forward(250)
t.left(90)
t.pendown()

# letra m
t.forward(100)
t.backward(100)
t.left(45)
t.forward(50)
t.left(90)
t.forward(50)
t.right(135)
t.forward(100)

# reposicionando
t.penup()
t.left(90)
t.forward(25)
t.left(90)
t.pendown()

# letra i
t.forward(100)

# reposicionando
t.penup()
t.right(90)
t.forward(25)
t.right(90)
t.pendown()

# letra l
t.forward(100)
t.left(90)
t.forward(50)

# reposicionando
t.penup()
t.forward(25)
t.left(90)
t.pendown()

# letra e
t.forward(100)
t.right(90)
t.forward(50)
t.penup()
t.right(90)
t.forward(50)
t.right(90)
t.pendown()
t.forward(50)
t.penup()
t.left(90)
t.forward(50)
t.left(90)
t.pendown()
t.forward(50)

# reposicionando
t.penup()
t.forward(25)
t.left(90)
t.pendown()

# letra n
t.forward(100)
t.right(145)
t.forward(122.5)
t.left(145)
t.forward(100)

# reposicionando
t.penup()
t.backward(100)
t.right(90)
t.forward(25)
t.left(60)
t.pendown()

#letra a
t.forward(117.5)
t.right(120)
t.forward(117.5)
t.backward(58.75)
t.right(120)
t.forward(50)

tela.exitonclick()