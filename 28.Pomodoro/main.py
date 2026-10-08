from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
reps = 0
timer = None
isReset = False

# ---------------------------- RESET BUTTON ------------------------------- # 
def reset_timer():
    global reps 
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text = '00:00')
    title_label.config(text="Timer",fg=GREEN)
    check_marks.config(text="")
    reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global isReset
    global reps
    reps += 1
    isReset == False
    start_timer()

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    if reps %8 == 0 and reps != 0:
        time = LONG_BREAK_MIN * 60
        title_label.config(text="Break",fg=PINK)
    elif reps %2 == 0:
        time = WORK_MIN * 60
        title_label.config(text="Timer",fg=GREEN)
    else:
        title_label.config(text="Break",fg=PINK)
        time = SHORT_BREAK_MIN *60
    count_down(time)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    global isReset
    mins = count//60
    secs = count % 60

    if secs <10:
        secs = f"0{secs}"
    canvas.itemconfig(timer_text,text= f"{mins}:{secs}")
    if count == 0:
        isReset = True
        if reps %2 == 0:
            check_marks.config(text='✅'*(int(reps/2)+1))
        reset()
    if count>0:
        timer = window.after(1000,count_down,count-1)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

title_label = Label(text="Timer",font=(FONT_NAME,45,'bold'))
title_label.config(bg=YELLOW,fg=GREEN)
title_label.grid(row=0,column=1)

canvas = Canvas(width = 200,height=224)
tomato_img= PhotoImage(file='tomato.png')
canvas.create_image(100,112,image = tomato_img)
canvas.config(bg=YELLOW,highlightthickness=0)
timer_text = canvas.create_text(100,132,text='00:00',fill='white',font=(FONT_NAME,35,'bold'))
canvas.grid(row=1,column=1)

start_button = Button(text="Start",highlightthickness=0,width=4,height=2,command=start_timer)
start_button.config(font=(FONT_NAME,16,"bold"))
start_button.grid(column=0,row=2)

reset_button = Button(text="Reset",highlightthickness=0,width=4,height=2,command=reset_timer)
reset_button.config(font=(FONT_NAME,16,"bold"),fg=RED,bg=YELLOW)
reset_button.grid(column=2,row=2)

check_marks = Label(text='',fg=GREEN,bg=YELLOW)
check_marks.grid(column=1,row = 3)

window.mainloop()