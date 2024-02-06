from tkinter import *

janela = Tk()
janela.title('Teste')
janela.minsize(width=500, height=300)

label = Label(text='Hello, World!', font=('Consolas', 20, 'bold'))
label.pack(side='top')

caixa_texto = Entry(width=20)
caixa_texto.pack()


def mudar_label():
    label.config(text=caixa_texto.get())


botao = Button(text='Botão Teste', width=25, height=2, command=mudar_label)
botao.pack(side='bottom')

janela.mainloop()
