from tkinter import *
from time import sleep


def countdown(minutes, seconds=0):
    seconds += minutes * 60
    for i in range(seconds + 1):
        global keep_counting
        if keep_counting:
            mins, secs = divmod(seconds - i, 60)
            time.config(text=f'{mins:02d}:{secs:02d}')
            sleep(1)
            window.update()
        else:
            main_label.config(text='Timer')


def work_time():
    global keep_counting
    keep_counting = True
    for i in range(4):
        main_label.config(text='Work')
        countdown(25)
        if i < 3:
            break_time(5)
        else:
            break_time(15)


def break_time(mins, secs=0):
    main_label.config(text='Break')
    countdown(mins, secs)


def reset_time():
    global keep_counting
    keep_counting = False
    main_label.config(text='Timer')
    time.config(text='00:00')


keep_counting = True

window = Tk()
window.title('Pomodoro')
window.config(padx=30, pady=30)
window.resizable(width=FALSE, height=FALSE)

main_label = Label(window, text='Timer', font=('Small Fonts', 50, 'bold'))
main_label.grid(column=1, row=0)

image = PhotoImage(file='tomato.png')
tomato = Label(window, image=image)
tomato.grid(column=1, row=1, padx=20, pady=20)

time = Label(window, text='00:00', font=('Small Fonts', 30, 'bold'), background='#c1c1c1')
time.grid(column=1, row=1)

start_button = Button(window, text='Start', font=('Small Fonts', 20), width=6, command=work_time)
start_button.grid(column=0, row=2)

reset_button = Button(window, text='Reset', font=('Small Fonts', 20), width=6, command=reset_time)
reset_button.grid(column=2, row=2)

window.mainloop()