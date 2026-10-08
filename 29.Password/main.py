from tkinter import *
from tkinter import messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    pw_letters = [random.choice(letters) for _ in range(nr_letters)]
    pw_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    pw_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    total_list = pw_letters + pw_numbers + pw_symbols
    random.shuffle(password_list)

    password =  "".join(total_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_creds():
    empty = False
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if website == '' or email == '' or password =='':
        empty = messagebox.askretrycancel(title="warning",message="Fields cannot be empty")

    if not empty:
        is_ok = messagebox.askokcancel(title=website,message="Save the details")

        if is_ok:
            with open('password.txt','a') as file:
                file.write(f"{website} | {email} | {password}\n")

            password_entry.delete(0,END)
            website_entry.delete(0,END)
            email_entry.delete(0,END)
            add_label.config(text='Added',padx=20)
            window.after(1000,lambda: add_label.config(text=''))

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manger")
window.config(padx=50,pady=50)

canvas = Canvas(height=250,width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)

website_label = Label(text="Website")
website_label.grid(row=1,column=0)

email_label = Label(text="Email/Username")
email_label.grid(row=2,column=0)

password_label = Label(text='Password')
password_label.grid(row=3,column=0)

add_label = Label(text="")
add_label.grid(row=5,column=1)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(row=3,column=1)

generate_button = Button(text='Generate',padx=18,width=5,command=generate_pass)
generate_button.grid(row=3,column=2)

add_button = Button(text="Add",width=35,command=save_creds)
add_button.grid(row=4,column=1,columnspan=2)

window.mainloop()