BACKGROUND_COLOR = "#B1DDC6"
import pandas
import random
from tkinter import *


    # datax=pandas.read_csv("")
data=pandas.read_csv("C:/Users/Admin/PycharmProjects/flashcardcapstone/flash-card-project-start/data/french_words.csv")
data_dict=data.to_dict()
test=data_dict["French"]
fword=list(test)
french_words=[test[word] for word in test]
teste=data_dict["English"]
English_words=[teste[word] for word in teste]
ind=random.choice(french_words)


window=Tk()
window.title("The flashcard capstone project")
window.minsize(width=850,height=600)
window.config(pady=50,padx=50,bg=BACKGROUND_COLOR)


def change(name):
    canvas.itemconfig(old_image,image=image_back)
    canvas.itemconfig(title,text="English",fill="white")
    index = french_words.index(name)
    canvas.itemconfig(tp,fill="white",text=English_words[index])


def right():
    canvas.itemconfig(old_image, image=image_front)
    rex = random.choice(french_words)
    window.after_cancel(window.after(3000, change,rex))
    canvas.itemconfig(tp,text=rex,fill="black")
    canvas.itemconfig(title,fill="black",text="French")
    window.after(3000, change,rex)
    words_list.append(rex)





canvas=Canvas(height=546,width=820,bg=BACKGROUND_COLOR)
image_front=PhotoImage(file="C:/Users/Admin/PycharmProjects/flashcardcapstone/flash-card-project-start/images/card_front.png")
image_back=PhotoImage(file="C:/Users/Admin/PycharmProjects/flashcardcapstone/flash-card-project-start/images/card_back.png")
old_image=canvas.create_image(420,270,image=image_front)
canvas.grid(columnspan=2,column=1,row=1)
title=canvas.create_text(400,150,font=("Arial",40,"italic"),text="French")
tp=canvas.create_text(400,263,font=("Arial",60,"bold"),text=ind)
window.after(3000, change,ind)
canvas.config(highlightthickness=0)

right_image=PhotoImage(file="C:/Users/Admin/PycharmProjects/flashcardcapstone/flash-card-project-start/images/right.png")
right_button=Button(image=right_image,highlightthickness=0,bg=BACKGROUND_COLOR,command=right)
right_button.grid(row=2,column=1)
wrong_image=PhotoImage(file="C:/Users/Admin/PycharmProjects/flashcardcapstone/flash-card-project-start/images/wrong.png")
wrong_button=Button(image=wrong_image,highlightthickness=0,bg=BACKGROUND_COLOR,command=right)
wrong_button.grid(row=2,column=2)






















window.mainloop()