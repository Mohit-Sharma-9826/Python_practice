from tkinter import *
from tkinter import messagebox
import random
import pyperclip    # This module is used to copy data in your clipboard.

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    passwd_entry.delete(0, END
                        )
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*','_','=', '+', '\\', '|', '<', '>', '/', '?']

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
    alert = messagebox.askyesno(title="Alert!", message="Do you wnat to add these details?")

    website = web_name_entry.get()
    name = user_name_entry.get()
    password = passwd_entry.get()

    if len(website) == 0 or len(password) == 0 or len(name) == 0:
        messagebox.showinfo(message="Please fill all details!")
        return

    if alert:
        with open("./TKinter/Password_Manager/PasswordData.txt", "a") as f:

            data = f"{website} | {name} | {password}\n"
            f.write(data)
        messagebox.showinfo(title="Infomer", message="Saved Successfully!")

    web_name_entry.delete(0, END)
    passwd_entry.delete(0, END)


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

web_name_entry = Entry(width=45)
web_name_entry.grid(column=1, row=1, columnspan=2)
web_name_entry.focus()

user_name = Label(text="Email/Username: ",font=("Arial", 15))
user_name.grid(column=0, row=2)

user_name_entry = Entry(width=45)
user_name_entry.grid(column=1, row=2, columnspan=2)
user_name_entry.insert(0, "mohit20064321@gmail.com")

passwd = Label(text="Password: ",font=("Arial", 15))
passwd.grid(column=0, row=3)

passwd_entry = Entry(width=21)
passwd_entry.grid(column=1, row=3)

gen_btn = Button(text="Generate Password", font=("Arial", 12), bg= "#cfcece", command=generate)
gen_btn.grid(column=2, row=3)

add_btn = Button(text="Add", font=("Arial", 12), bg= "#cfcece", width=40, command=pass_saver)
add_btn.grid(column=1, row=4, columnspan=2)


window.mainloop()