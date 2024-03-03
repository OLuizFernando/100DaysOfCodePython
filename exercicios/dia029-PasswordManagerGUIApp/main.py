from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    num_letters = randint(8, 10)
    num_symbols = randint(2, 4)
    num_numbers = randint(2, 4)

    password_letters = [choice(LETTERS) for _ in range(num_letters)]
    password_symbols = [choice(SYMBOLS) for _ in range(num_symbols)]
    password_numbers = [choice(NUMBERS) for _ in range(num_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = ''.join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


def save_password():
    website = website_entry.get().strip()
    email_username = email_username_entry.get().strip()
    password = password_entry.get().strip()

    if website != '' and email_username != '' and password != '':
        confirmation = messagebox.askyesno(title='Confirmation Dialog',
                                           message=f'''Are you sure you want to save the entered data?\n
                                           \nWebsite: {website}
                                           \nEmail/Username: {email_username}
                                           \nPassword: {password}''')

        if confirmation:
            with open('data.txt', 'a') as file:
                file.write(f'{website} | {email_username} | {password}\n')

            website_entry.delete(0, END)
            email_username_entry.delete(0, END)
            password_entry.delete(0, END)

    else:
        messagebox.showerror(title='Error', message="Please don't leave any fields blank.")


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

password_entry = Entry(width=23, font=('Arial', 15))
password_entry.grid(column=1, row=3, padx=10, pady=10)

generate_password_button = Button(text='Generate Password', command=generate_password)
generate_password_button.grid(column=2, row=3, padx=10, pady=10)

add_button = Button(text='Add', width=67, height=2, command=save_password)
add_button.grid(column=0, row=4, columnspan=3, padx=10, pady=20)

window.mainloop()