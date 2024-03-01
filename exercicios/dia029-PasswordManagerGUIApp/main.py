from tkinter import *

window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20, bg='black')
window.resizable(width=FALSE, height=FALSE)

image = PhotoImage(file='locker.png')
canvas = Canvas(width=150, height=260, bg='black', highlightthickness=0)
canvas.create_image(75, 96, image=image)
canvas.create_text(75, 230, text='MyPass', fill='white', font=('Times', 30, 'bold'))
canvas.grid(column=1, row=0, padx=10, pady=20)

website_label = Label(text='Website:', background='black', foreground='white', font=('Arial', 15))
website_label.grid(column=0, row=1, padx=10, pady=10)

website_entry = Entry(width=35, font=('Arial', 15))
website_entry.grid(column=1, row=1, columnspan=2, padx=10, pady=10)

email_username_label = Label(text='Email/Username:', background='black', foreground='white', font=('Arial', 15))
email_username_label.grid(column=0, row=2, padx=10, pady=10)

email_username_entry = Entry(width=35, font=('Arial', 15))
email_username_entry.grid(column=1, row=2, columnspan=2, padx=10, pady=10)

password_label = Label(text='Password:', background='black', foreground='white', font=('Arial', 15))
password_label.grid(column=0, row=3, padx=10, pady=10)

password_entry = Entry(width=19, font=('Arial', 15))
password_entry.grid(column=1, row=3, padx=10, pady=10)

generate_password_button = Button(text='Generate Password')
generate_password_button.grid(column=2, row=3, padx=10, pady=10)

add_button = Button(text='Add', width=67, height=2)
add_button.grid(column=0, row=4, columnspan=3, padx=10, pady=20)

window.mainloop()