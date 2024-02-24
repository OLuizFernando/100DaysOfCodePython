from tkinter import *


def work_time():
    main_label.config(text='Work')
    time.config(text='25:00')


def break_time():
    main_label.config(text='Break')
    time.config(text='05:00')


def reset_time():
    main_label.config(text='Timer')
    time.config(text='00:00')


window = Tk()
window.title('Pomodoro')
window.minsize(width=710, height=645)
window.config(padx=30, pady=30)

main_label = Label(text='Timer', font=('Small Fonts', 50, 'bold'))
main_label.grid(column=1, row=0)

image = PhotoImage(file='tomato.png')
tomato = Label(image=image)
tomato.grid(column=1, row=1, padx=20, pady=20)

time = Label(text='00:00', font=('Small Fonts', 30, 'bold'), background='#c1c1c1')
time.grid(column=1, row=1)

start_button = Button(text='Start', font=('Small Fonts', 20), width=6, command=work_time)
start_button.grid(column=0, row=2)

break_button = Button(text='Break', font=('Small Fonts', 20), width=6, command=break_time)
break_button.grid(column=1, row=2)

reset_button = Button(text='Reset', font=('Small Fonts', 20), width=6, command=reset_time)
reset_button.grid(column=2, row=2)

window.mainloop()