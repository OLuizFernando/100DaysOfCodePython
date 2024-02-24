from tkinter import *
from time import sleep


def countdown(minutes, seconds=0):
    seconds += minutes * 60
    for i in range(seconds + 1):
        global keep_counting
        if keep_counting:
            mins, secs = divmod(seconds - i, 60)
            time_label.config(text=f'{mins:02d}:{secs:02d}')
            sleep(1)
            window.update()
        else:
            main_label.config(text='Timer')
            time_label.config(text='00:00')
            update_checks(0)


def pomodoro_process():
    reps = 0
    global keep_counting
    keep_counting = True
    for i in range(4):
        work_time(25)

        reps += 1
        update_checks(reps)

        if i < 3:
            break_time(5)
        else:
            break_time(15)


def work_time(mins, secs=0):
    main_label.config(text='Work')
    countdown(mins, secs)


def break_time(mins, secs=0):
    main_label.config(text='Break')
    countdown(mins, secs)


def reset_time():
    global keep_counting
    keep_counting = False


def update_checks(reps):
    checks_label.config(text='✔' * reps)
    checks_label.place(x=(313 - reps * 6.5), y=525)


keep_counting = True

window = Tk()
window.title('Pomodoro')
window.minsize(width=710, height=645)
window.config(padx=30, pady=30)
window.resizable(width=FALSE, height=FALSE)

main_label = Label(window, text='Timer', font=('Small Fonts', 50, 'bold'))
main_label.place(x=235, y=0)
# main_label.grid(column=1, row=0)

image = PhotoImage(file='tomato.png')
tomato = Label(window, image=image)
tomato.place(x=125, y=100)
# tomato.grid(column=1, row=1, padx=20, pady=20)

time_label = Label(window, text='00:00', font=('Small Fonts', 30, 'bold'), background='#c1c1c1')
time_label.place(x=265, y=320)
# time.grid(column=1, row=1)

start_button = Button(window, text='Start', font=('Small Fonts', 20), width=6, command=pomodoro_process)
start_button.place(x=27, y=525)
# start_button.grid(column=0, row=2)

reset_button = Button(window, text='Reset', font=('Small Fonts', 20), width=6, command=reset_time)
reset_button.place(x=519, y=525)
# reset_button.grid(column=2, row=2)

checks_label = Label(window, text='', font=('Small Fonts', 15))
checks_label.place(x=313, y=525)

window.mainloop()