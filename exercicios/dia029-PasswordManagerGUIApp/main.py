from tkinter import *

window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20, bg='black')
window.resizable(width=FALSE, height=FALSE)

image = PhotoImage(file='locker.png')
canvas = Canvas(width=150, height=250, bg='black', highlightthickness=0)
canvas.create_image(75, 96, image=image)
canvas.create_text(75, 230, text='MyPass', fill='white', font=('Times', 30, 'bold'))
canvas.grid(column=0, row=0)

window.mainloop()