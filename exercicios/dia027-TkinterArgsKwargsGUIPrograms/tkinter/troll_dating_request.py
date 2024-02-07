from tkinter import *
from random import randint


def mudar_posicao():
    nao.place(relx=0, rely=0, x=randint(25, 1215), y=randint(15, 665))


def escolha_certa():
    sim.destroy()
    nao.destroy()
    pergunta.config(text='Parabéns! Você fez a escolha certa.', font=('Small Fonts', 40))
    pergunta.place(relx=0.5, rely=0.5, anchor=CENTER)


janela = Tk()
janela.minsize(width=1280, height=720)
janela.config(padx=10, pady=10, background='pink')

pergunta = Label(text='Quer namorar comigo?', font=('Small Fonts', 20), background='pink')
pergunta.place(relx=0.5, rely=0.4, anchor=CENTER)

sim = Button(text='Sim', width=20, font=('Small Fonts', 15), command=escolha_certa)
sim.place(relx=0.5, rely=0.475, anchor=CENTER)

nao = Button(text='Não', width=5, height=2, font=('Small Fonts', 10), command=mudar_posicao)
nao.place(relx=0.5, rely=0.55, anchor=CENTER)

janela.mainloop()