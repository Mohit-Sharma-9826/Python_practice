from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
tick = "✔️"
check_marks_x = 90
time = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    global tick
    global check_marks_x

    window.after_cancel(time)

    canvas.itemconfig(can_text, text="00:00")

    window.title("Promodoro")
    timer.config(text="Timer", fg=GREEN)

    check_marks.config(text="")

    reps = 0
    tick = "✔️"
    check_marks_x = 90


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    global tick
    global check_marks_x
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps <= 8:
        if reps%8 == 0:
            countdown(long_break_sec, "Long Break", RED)
        elif reps%2 == 0:
            countdown(short_break_sec, "Short Break", PINK)
            check_marks.config(text=tick)
            tick += "✔️"
            check_marks.place(x=check_marks_x, y=310)
            check_marks_x -= 20
        else:
            countdown(work_sec, "Work Time", GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count, head, color):
    min = count // 60
    sec = count % 60

    str_min = str(min)
    str_sec = str(sec) if sec>=10 else "0"+str(sec)

    canvas.itemconfig(can_text, text=f"{str_min}:{str_sec}")
    timer.config(text=head, fg=color)
    if min >= 0 and sec > 0:
        global time
        time = window.after(1000, countdown, count-1, head, color)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Promodoro")
window.config(padx=100, pady=50, bg=YELLOW)
window.minsize(width=300, height=450)

timer = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 30, "bold"), bg=YELLOW)
timer.pack()

# Fetching the tomato image and displaying on the screen using canvas widget.
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="./Tkinter/promodore_start/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
can_text = canvas.create_text(103, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.pack()

# Adding buttons to the bottom.
btn1 = Button(text="Start", font=(FONT_NAME, 8, "bold"), highlightthickness=0, command=start_timer)
btn1.place(x=-20, y=280)
btn2 = Button(text="Reset", font=(FONT_NAME, 8, "bold"), highlightthickness=0, command=reset_timer)
btn2.place(x=180, y=280)

# Adding the check_marks.
check_marks = Label(font=(FONT_NAME, 15, "bold"), bg=YELLOW, highlightthickness=0, fg=GREEN)
check_marks.place(x=90, y=310)

window.mainloop()
