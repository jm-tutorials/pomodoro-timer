from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
ROUNDS = 8
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "✓"
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    remove_checkmarks()

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1
    if reps < 0:
        return
    if reps % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    elif reps % ROUNDS == 0:
        timer_label.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    else:
        timer_label.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def format_time(time_unit):
    return str(int(time_unit)).zfill(2)


def count_down(count):
    minutes = count // 60
    seconds = count % 60
    canvas.itemconfig(timer_text, text="{}:{}".format(format_time(minutes),format_time(seconds)))
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        add_checkmark(reps//2)


# ---------------------------- ADD/REMOVE CHECKMARK functions ------------------------------- #


def add_checkmark(marks=None):
    if marks and type(marks) == int:
        check_mark_label.config(text=CHECKMARK*marks)


def remove_checkmarks():
    check_mark_label.config(text="")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME,35,"bold"))

canvas.grid(row=1, column=1)

# labels
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
timer_label.grid(row=0, column=1)

check_mark_label = Label(text="", fg=GREEN, bg=YELLOW)
check_mark_label.grid(row=3, column=1)

# buttons
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

window.mainloop()