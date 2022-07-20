THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

class Quizinterface:

    def __init__(self,quiz_brain):
        def correct(self):
            self.quiz.check_answer("True")
        self.quiz=quiz_brain
        self.score=0
        self.window=Tk()
        self.window.title("Quizzler")
        self.window.minsize(height=450,width=350)
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)
        self.canvas=Canvas(height=250,width=300,bg="white")
        self.canvas.grid(row=2,column=1,columnspan=2,pady=50)
        self.label=Label(text=f"Score={self.score}",fg="white",bg=THEME_COLOR)
        self.label.grid(row=1,column=2)
        self.question_text=self.canvas.create_text(137,105,text="Question",fill="black",font=("Arial",20,"italic"),width=280)
        true=PhotoImage(file="C:/Users/Admin/PycharmProjects/quizzler/quizzler-app-start/images/true.png")
        false=PhotoImage(file="C:/Users/Admin/PycharmProjects/quizzler/quizzler-app-start/images/false.png")
        self.right=Button(image=true,command=correct)
        self.right.grid(row=3,column=1)
        self.wrong=Button(image=false)
        self.wrong.grid(row=3,column=2)




        self.get_next_question()

        self.window.mainloop()
    def get_next_question(self):
        qtext=self.quiz.next_question() #Important
        self.canvas.itemconfig(self.question_text,text=qtext)



