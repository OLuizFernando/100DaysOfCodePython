from tkinter import *


def mudar_label():
    if textinho.get().strip() != '':
        label.config(text=textinho.get().strip())
    print(textinho.get().strip())
    print(textao.get('1.0', END).strip())
    print(spinbox.get())
    print(escala.get())
    print(checkbox_estado.get())
    print(escolha_estado.get())
    print(lista.get(lista.curselection()))


janela = Tk()
janela.title('Teste')
janela.minsize(width=450, height=450)

label = Label(text='Hello, World!')
label.pack(side='top')

botao = Button(text='Botão Teste', width=10, height=1, command=mudar_label)
botao.pack()

textinho = Entry(width=20)
textinho.insert(index=END, string='digite um textinho')
textinho.pack()

textao = Text(height=5, width=10)
textao.insert(index=END, chars='digite um textão')
textao.pack()

spinbox = Spinbox(from_=0, to=10, width=10)
spinbox.pack()

escala = Scale(from_=100, to=0)
escala.pack()


checkbox_estado = IntVar()
checkbox = Checkbutton(text='Não sou um robô', variable=checkbox_estado)
checkbox.pack()

escolha_estado = IntVar()
escolha1 = Radiobutton(text='Opção 1', value=1, variable=escolha_estado)
escolha1.pack()
escolha2 = Radiobutton(text='Opção 2', value=2, variable=escolha_estado)
escolha2.pack()

lista = Listbox(height=3)
opcoes = ['Lenovo Ideapad 3', 'Dell Latitude 3410', 'Asus Vivobook 16']
for opcao in opcoes:
    lista.insert(opcoes.index(opcao), opcao)
lista.bind('<<ListboxSelect>>')
lista.pack()

janela.mainloop()
