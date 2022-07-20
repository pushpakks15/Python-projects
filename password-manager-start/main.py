# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list_of_letters = [random.choice(letters) for char in range(nr_letters)]

    password_list_of_symbols = [random.choice(symbols) for sym in range(nr_symbols)]

    password_list_of_numbers = [random.choice(numbers) for num in range(nr_numbers)]

    password_list = password_list_of_numbers + password_list_of_symbols + password_list_of_letters

    random.shuffle(password_list)

    password = "".join(password_list)
    entry_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def info():
    website = entry_web.get()
    gmail = entry_user.get()
    password = entry_password.get()
    new_data = {website: {"email": gmail, "password": password}}
    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please do not leave any fields empty. ")
    else:
        try:
            with open(file="info.json", mode="r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open(file="info.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            #Remember data is a variable and a seperate value
            with open(file="info.json", mode="w") as file:
                json.dump(data, file, indent=4)
        finally:
            entry_password.delete(0, END)
            entry_web.delete(0, END)

def find_password():
    with open(file="info.json",mode="r") as file:
        data=json.load(file)
        website = entry_web.get()
        try:
            messagebox.showinfo(title=website,message=f"email:{data[website]['email']}\n password:{data[website]['password']}")
        except:
            messagebox.showerror(title="website",message="No data file found")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("PASSWORD MANAGER")
window.config(height=220, width=420)
window.config(padx=40, pady=40)

canvas = Canvas(height=200, width=200, highlightthickness=2, borderwidth=20)
image_p = PhotoImage(file="logo.png")
canvas.create_image(100, 120, image=image_p)
canvas.grid(column=2, row=0)

website_label = Label(text="Website:")
website_label.grid(column=1, row=1,sticky=E)

username_label = Label(text="Email/Username:")
username_label.grid(column=1, row=2,sticky=E)

password_label = Label(text="Password:")
password_label.grid(column=1, row=3,sticky=E)

entry_web = Entry(width=39)
entry_web.grid(column=2, row=1,sticky=W)

search_button=Button(text="Search",width=20,command=find_password)
search_button.grid(row=1,column=3,sticky=W)

entry_web.focus()
entry_user = Entry(width=65)
entry_user.grid(column=2, row=2, columnspan=2,sticky=W)

entry_user.insert(0, "pushpak.22010400@viit.ac.in")
entry_password = Entry(width=39)

entry_password.grid(column=2, row=3,sticky=W)

password = Button(text="Generate Password", command=gen_pass,width=20)
password.grid(column=3, row=3)

add = Button(text="Add", width=36, command=info)
add.grid(column=2, row=4, columnspan=2,sticky=S)

window.mainloop()
