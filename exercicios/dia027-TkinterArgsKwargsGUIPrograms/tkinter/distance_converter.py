from tkinter import *


def formatar(m):
    try:
        return int(m)
    except ValueError:
        try:
            return float(m.replace(',', '.'))
        except ValueError:
            return 'Inválido'


def calcular():
    m = formatar(m_input.get())
    if m != 'Inválido':
        km = m * 1.609
        km_output.config(text=round(km, 2))
    else:
        km_output.config(text=m)


window = Tk()
window.title('Conversor de Distância')
window.minsize(width=335, height=160)
window.config(padx=20, pady=20)

label_igual = Label(text='é igual à:', font=('Arial', 15))
label_igual.grid(column=0, row=1, padx=5, pady=5)

m_input = Entry(width=10, font=('Arial', 15))
m_input.grid(column=1, row=0, padx=5, pady=5)

km_output = Label(text=0, font=('Arial', 15))
km_output.grid(column=1, row=1, padx=5, pady=5)

button = Button(text='Calcular', font='Arial', width=12, command=calcular)
button.grid(column=1, row=2, padx=5, pady=5)

label_milhas = Label(text='Milhas', font=('Arial', 15))
label_milhas.grid(column=2, row=0, padx=5, pady=5)

label_km = Label(text='Km', font=('Arial', 15))
label_km.grid(column=2, row=1, padx=5, pady=5)

window.mainloop()