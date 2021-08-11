from tkinter import *
import math

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
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    start_button.config(command=start_timer)
    window.after_cancel(timer)
    reps = 0
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    checkmark_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    start_button.config(command=reset_timer)
    window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text="Enjoy a break!", fg=GREEN)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text="Enjoy a break!", fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        timer_label.config(text="Time to Work!", fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    # Dynamic typing
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        checkmark_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
window.eval('tk::PlaceWindow . center')

canvas = Canvas(width=204, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

timer_label = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

start_button = Button(text="Start", command=start_timer, highlightbackground=YELLOW)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=reset_timer, highlightbackground=YELLOW)
reset_button.grid(row=2, column=2)

checkmark_label = Label(font=(FONT_NAME, 32), fg=GREEN, bg=YELLOW)
checkmark_label.grid(row=3, column=1)

window.mainloop()
