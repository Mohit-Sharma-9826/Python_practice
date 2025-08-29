from tkinter import *
from tkinter import messagebox
import random
import json
import pyperclip    # This module is used to copy data in your clipboard.

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    passwd_entry.delete(0, END
                        )
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*','_','=', '+', '|', '<', '>', '/', '?']

    n_letter = random.randint(8, 10)
    n_number = random.randint(2, 4)
    n_sym = random.randint(2, 4)

    total = n_letter + n_number + n_sym
    password = ""
    ch = [letters, numbers, symbols]

    while len(password) != total:
        ran = random.choice(ch)
        if ran == ch[0]:
            password += random.choice(ran)
            n_letter -= 1
        elif ran == ch[1]:
            password += random.choice(ran)
            n_number -= 1
        else:
            password += random.choice(ran)
            n_sym -= 1
    
    pyperclip.copy(password)     #Here we are coping data to the clipboard.
    passwd_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def pass_saver():
    alert = True #messagebox.askyesno(title="Alert!", message="Do you wnat to add these details?")

    website = web_name_entry.get()
    name = user_name_entry.get()
    password = passwd_entry.get()

    data = {
        website: {
            "email": name,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0 or len(name) == 0:
        messagebox.showinfo(message="Please fill all details!")
        return

    if alert:
        try:
            with open("./TKinter/Password_Manager/PasswordData.json", "r") as f:
                try:
                    new_data = json.load(f)
                    new_data.update(data)
                except json.JSONDecodeError:
                    new_data = data
        except FileNotFoundError:
            new_data = data
        
        with open("./TKinter/Password_Manager/PasswordData.json", "w") as f:
            json.dump(new_data, f, indent=4)

        messagebox.showinfo(title="Infomer", message="Saved Successfully!")

    web_name_entry.delete(0, END)
    passwd_entry.delete(0, END)


# ---------------------------- Searching ------------------------------- #
def search():
    website = web_name_entry.get()
    
    user_name_entry.delete(0, END)
    passwd_entry.delete(0, END)

    try:
        with open("./TKinter/Password_Manager/PasswordData.json", "r") as f:
            try:
                file_data = json.load(f)
                data = file_data[website]
                user_name_entry.insert(0, data["email"])
                passwd_entry.insert(0, data["password"])
            
            except KeyError:
                messagebox.showinfo(message=f"{website} record does not exist!")

    except FileNotFoundError:
        messagebox.showinfo(message="No records are saved yet!")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="./TKinter/Password_Manager/logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

web_name = Label(text="Website: ",font=("Arial", 15))
web_name.grid(column=0, row=1)

web_name_entry = Entry(width=34)
web_name_entry.grid(column=1, row=1)
web_name_entry.focus()

search_btn = Button(text="Search", font=("Arial", 15), bg= "#cfcece", width=12)
search_btn.grid(column=2, row=1)

user_name = Label(text="Email/Username: ",font=("Arial", 15))
user_name.grid(column=0, row=2)

user_name_entry = Entry(width=60)
user_name_entry.grid(column=1, row=2, columnspan=2)
user_name_entry.insert(0, "mohit20064321@gmail.com")

passwd = Label(text="Password: ",font=("Arial", 15))
passwd.grid(column=0, row=3)

passwd_entry = Entry(width=34)
passwd_entry.grid(column=1, row=3)

search_btn.config(command=search)

gen_btn = Button(text="Generate Password", font=("Arial", 12), bg= "#cfcece", command=generate)
gen_btn.grid(column=2, row=3)

add_btn = Button(text="Add", font=("Arial", 12), bg= "#cfcece", width=40, command=pass_saver)
add_btn.grid(column=1, row=4, columnspan=2)


window.mainloop()