import turtle as t

s = t.Screen()
s.title('Brazil States Game')
imagem = 'mapa.gif'
s.addshape(imagem)
t.shape(imagem)


def get_mouse_click_coor(x, y):
    print(x, y)


t.onscreenclick(get_mouse_click_coor)

t.mainloop()
