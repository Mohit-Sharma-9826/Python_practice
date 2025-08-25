import tkinter

window = tkinter.Tk()
window.title("First GUI program")
window.minsize(width=500, height=300)

# <---------- Widgets ---------->

#Label
lb = tkinter.Label(text="I am a Label!", font=("Arial", 18, "bold"))
lb.pack(side="top")     # The default id side="top"
# lb.pack(expand=True)

lb["text"] = "New Text"        # Process-1 Modifying the text of label


# Entry
inp = tkinter.Entry(width=20)
inp.insert(tkinter.END, string="write anything")
inp.place(x=100, y=200)

# Button
def clicked():
    print("I got clicked!")
    val = inp.get()
    lb.config(text=val)  # Process-2 Modifying the text of label

button = tkinter.Button(text="Click me", command=clicked, bg="skyblue", fg="red")
button.pack()


# Text
txt = tkinter.Text(height=5, width=30)
txt.focus()
txt.insert(tkinter.END, "This is the exampe of text.")
print(txt.get("1.0", tkinter.END))
txt.pack()


# Spinbox
def spin():
    print(sp.get())


sp = tkinter.Spinbox(from_=0, to=10, width=5, command=spin)
sp.pack()


# Scale
def scale(value):
    print(value)

sc = tkinter.Scale(from_=0, to=100, command=scale)
sc.pack()


# CheckButton
def check():
    print(checked_state.get())

checked_state = tkinter.IntVar()
ch_btn = tkinter.Checkbutton(text="Is it on?", variable=checked_state, command=check)
checked_state.get()
ch_btn.pack()


# RadioButton
def radio_use():
    print(radio_state.get())

radio_state = tkinter.IntVar()
rd_btn1 = tkinter.Radiobutton(text="Option1", value=10, variable=radio_state, command=radio_use)
rd_btn2 = tkinter.Radiobutton(text="Option2", value=20, variable=radio_state, command=radio_use)
rd_btn1.pack()
rd_btn2.pack()


# ListBox
def listbox_use():
    selected = lsbox.curselection()
    if selected:
        print(lsbox.get(selected[0]))


lsbox = tkinter.Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    lsbox.insert(tkinter.END, item)

lsbox.bind("<<ListboxSelect>>", listbox_use)
lsbox.pack()

window.mainloop()