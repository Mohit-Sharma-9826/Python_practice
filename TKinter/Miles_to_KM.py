from tkinter import *

window = Tk()
window.title("Miles to KM")
window.minsize(width=400, height=200) 

def display():
    miles = int(inp.get())
    km = miles*1.609344
    label3.config(text=f"{km:.2f}") 

inp = Entry(width=20)
inp.grid(column=1, row=0)

label1 = Label(text="Miles", font=("Arial", 20))
label1.grid(column=2, row=0)

label2 = Label(text="is equal to", font=("Arial", 20))
label2.grid(column=0, row=1)

label3 = Label(text="0", font=("Arial", 20))
label3.grid(column=1, row=1)

label4 = Label(text="Km", font=("Arial", 20))
label4.grid(column=2, row=1)

btn = Button(text="Calculate", font=("Arial", 20), command=display)
btn.grid(column=1, row=2)


window.mainloop()