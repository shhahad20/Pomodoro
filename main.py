import math
from tkinter import *
import time
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
TIMER = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(TIMER)
    canvas.itemconfig(t, text="00:00")
    check_mark.config(text="")
    label.config(text="Timer", fg=GREEN)
    global reps
    reps =0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps +=1
    work = WORK_MIN * 60
    break_ = SHORT_BREAK_MIN * 60
    longBreak = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(longBreak)
        label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(break_)
        label.config(text= "Break", fg=PINK)

    else:
        count_down(work)
        label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec =f"0{count_sec}"
    canvas.itemconfig(t, text=f"{count_min}:{count_sec}")
    if count > 0:
        global TIMER
        TIMER =window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks =""
        sessions = math.floor(reps/2)
        for _ in range(sessions):
            marks+= "✔"
        check_mark.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Timer")
window.minsize(width=500, height=500)
window.config(padx=20, pady=20, bg=YELLOW)

label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
label.grid(column=3, row=0)


canvas = Canvas(width=205, height=225, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato_img)
t = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=3, row=3)


start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(column=1, row=5)
reset_button = Button(text="Reset", highlightthickness=0, command=reset)
reset_button.grid(column=6, row=5)

check_mark = Label(text="", fg=GREEN, font=(FONT_NAME, 15, "bold"), bg=YELLOW)
check_mark.grid(column=3, row=6)

window.mainloop()
