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
reps=0
timer=None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_txt,text="00:00")
    label1.config(text="TIMER")
    label2.config(text="")
    global reps
    reps=0
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start():
    global reps
    reps+=1
    work=WORK_MIN*60
    long=LONG_BREAK_MIN*60
    short = SHORT_BREAK_MIN * 60
    if reps % 8 == 0:
        countdown(long)
        label1.config(text="LONG BREAK",fg=RED)
    elif reps %2==0:
        countdown(short)
        label1.config(text="SHORT BREAK", fg=PINK)
    else:
        countdown(work)
        label1.config(text="WORK", fg=GREEN)




def countdown(count):
    count_min=math.floor(count/60)
    count_sec=count % 60
    if count_sec<10:
        count_sec=f"0{count_sec}"

    canvas.itemconfig(timer_txt,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer=window.after(1000,countdown,count-1)
    else:
        start()
        marks=""
        work_sessions=math.floor(reps/2)
        for a in range(work_sessions):
            marks+="✔"
            label2.config(text=marks)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(height=230,width=244)
window.config(padx=50,pady=100,bg=YELLOW)


canvas=Canvas(height=230,width=244,bg=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(105,115,image=tomato_img)
timer_txt=canvas.create_text(100,125,text="00:00",fill="white",font=(FONT_NAME,24,"bold"))
canvas.grid(column=2,row=2)


label1=Label(text="TIMER",font=(FONT_NAME,24,"bold"),fg=GREEN,bg=YELLOW)
label1.grid(column=2,row=1)
button=Button(text="START",font=(FONT_NAME,15,"bold"),bg=YELLOW,command=start)
button.grid(column=1,row=3)
reset=Button(text="RESET",font=(FONT_NAME,15,"bold"),bg=YELLOW,command=reset_timer)
reset.grid(column=3,row=3)

label2=Label(font=(FONT_NAME,24,"bold"),fg=GREEN,bg=YELLOW)
label2.grid(column=2,row=4)













window.mainloop()