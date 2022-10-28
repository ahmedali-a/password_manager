from tkinter import messagebox
from tkinter import *
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_entry():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="You have an empty field!")
    else:
        is_ok = messagebox.askokcancel(title=website, message="These are the details entered:\n"
                                                              f"Email: {username}\n"
                                                              f"Password: {password}\n"
                                                              f"Is this ok to save?")
        if is_ok:
            with open("password_data.txt", 'a') as data:
                data.write(f"{website} | {username} | {password}\n")
            password_input.delete(0, END)
            website_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
screen = Tk()
screen.title("Password Manager")
screen.config(pady=30, padx=30)

# Canvas creation
my_canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
my_canvas.create_image(100, 100, image=logo_img)
my_canvas.grid(column=1, row=0)

# Generate Button creation
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=add_entry)
add_button.grid(column=1, row=4, columnspan=2)

# Text on screen generation
website_text = Label(text="Website:")
website_text.grid(column=0, row=1)

username_text = Label(text="Email/Username:")
username_text.grid(column=0, row=2)

password_text = Label(text="Password:")
password_text.grid(column=0, row=3)

# Generate text inputs
website_input = Entry(width=35)
website_input.focus()
website_input.grid(column=1, row=1, columnspan=2)

password_input = Entry(width=21)
password_input.grid(column=1, row=3)

username_input = Entry(width=35)
username_input.insert(0, "Ahmedali-a@hotmail.com")
username_input.grid(column=1, row=2, columnspan=2)

screen.mainloop()
