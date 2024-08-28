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

def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text = "00:00")
    label.config(text = "Timer",font = (FONT_NAME,30,"bold"),fg = GREEN )
    check_mark.config(text = "")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    #if it's the 8th rep
    if reps % 8 == 0:
        label.config(text ="Take a long break.", font = (FONT_NAME,30,"bold"), fg = RED)
        countdown(long_break_sec)
    
    #if it's the 2nd/4th/6th rep
    elif reps % 2 == 0:
        label.config(text ="TIME FOR A BREAK!", font = (FONT_NAME,30,"bold"), fg = PINK)
        countdown(short_break_sec)
        
    #If it's the 1st/3rd/5th/7th res
    else:
         label.config(text ="WORK.", font = (FONT_NAME,30,"bold"), fg = GREEN)
         countdown(work_sec)
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60 
    if count_sec == 0:
        count_sec = f"0{count_sec}"
        
    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer = window.after(1000,countdown,count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        
        for i in range(work_sessions):
            marks += "✅"
        
        check_mark.config(text = marks)

# ---------------------------- UI SETUP ------------------------------- #

#Window
window = Tk()
window.title("Pomodoro")
window.config(padx = 100, pady = 50, bg = YELLOW)

#Tomato
canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness = 0)
tomato = PhotoImage(file = "tomato.png")
canvas.create_image(100,112,image = tomato)
timer_text = canvas.create_text(100,112,text = "00:00",fill = "white", font = (FONT_NAME,35,"bold"))
canvas.grid(column = 1,row = 1)  

#Label
label = Label(text = "Timer",font = (FONT_NAME,30,"bold"),fg = GREEN)
label.grid(column = 1, row = 0)

check_mark = Label(fg = GREEN)
check_mark.grid(column = 1, row = 3)

#Buttons
start_button = Button(text = "Start",command = start_timer)
start_button.grid(column = 0, row = 2)
reset_button = Button(text = "Reset", command = reset)
reset_button.grid(column = 2, row = 2)





window.mainloop()