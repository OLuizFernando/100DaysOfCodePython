from tkinter import *

window = Tk()
window.title('Teste')
window.minsize(width=500, height=300)

label = Label(text='Label', font=('Consolas', 40, 'bold'))
label.grid(column=0, row=0)

button = Button(text='Button', height=5, width=10)
button.grid(column=1, row=1)

new_button = Button(text='New Button', height=5, width=10)
new_button.grid(column=2, row=0)

entry = Text(width=10, height=4)
entry.grid(column=3, row=2)

window.mainloop()