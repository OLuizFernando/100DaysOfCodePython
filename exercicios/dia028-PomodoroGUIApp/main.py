from tkinter import *


def countdown(count):
    global keep_counting
    if keep_counting:
        minutes = count // 60
        seconds = count % 60
        time_label.config(text=f'{minutes:02d}:{seconds:02d}')
        if count > 0:
            window.after(1000, countdown, count - 1)
        else:
            pomodoro_process()


def pomodoro_process():
    global step
    global reps
    global keep_counting
    keep_counting = True
    if step in [0, 2, 4, 6]:
        work_time(25)
        reps += 1
        step += 1

    elif step in [1, 3, 5]:
        break_time(5)
        update_checks()
        step += 1

    elif step == 7:
        break_time(20)
        update_checks()
        step += 1


def work_time(mins):
    secs = mins * 60
    main_label.config(text='Work')
    countdown(secs)


def break_time(mins):
    secs = mins * 60
    main_label.config(text='Break')
    countdown(secs)


def reset():
    global step
    global reps
    global keep_counting
    keep_counting = False
    main_label.config(text='Timer')
    time_label.config(text='00:00')
    step = 0
    reps = 0
    update_checks()


def update_checks():
    global reps
    checks_label.config(text='✔' * reps)
    checks_label.place(x=(313 - reps * 6.5), y=525)


step = 0
reps = 0
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

reset_button = Button(window, text='Reset', font=('Small Fonts', 20), width=6, command=reset)
reset_button.place(x=519, y=525)
# reset_button.grid(column=2, row=2)

checks_label = Label(window, text='', font=('Small Fonts', 15))
checks_label.place(x=313, y=525)

window.mainloop()