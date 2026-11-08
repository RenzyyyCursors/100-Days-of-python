from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx= 20,pady= 20, bg = THEME_COLOR)

        self.score_label = Label(text="Score: 0" , fg= "white",bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)

        self.canvas = Canvas(width= 300, height= 250, bg="white")
        self.question_text = self.canvas.create_text(150,125,text= "",
                                                    width=280,
                                                    fill=THEME_COLOR,
                                                    font=("Arial",20,"italic"))
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        true_image = PhotoImage(file= "images/true.png")
        self.true_button = Button(image=true_image,highlightthickness=0,command= lambda: self.verify_answer(True))
        self.true_button.grid(row=2,column=1)

        false_image = PhotoImage(file= "images/false.png")
        self.false_button = Button(image=false_image,highlightthickness=0,command=lambda: self.verify_answer(False))
        self.false_button.grid(row=2,column=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text,text= q_text)

    def end_app(self):
        self.window.destroy()

    def default_background(self):
        self.canvas.config(bg= "white")

    def verify_answer(self,answer):
        accurate = self.quiz.check_answer(answer)
        self.score_label.config(text= f"{self.quiz.score}/10")

        if accurate:
            self.canvas.config(bg= "green")
        else:
            self.canvas.config(bg= "red")
        self.window.after(ms=250,func=self.default_background)

        if self.quiz.still_has_questions():
            self.get_next_question()
        else:
            self.true_button.destroy()
            self.false_button.destroy()
            self.score_label.destroy()
            self.canvas.itemconfig(self.question_text,text= f"You quiz score is \n{self.quiz.score}/10")

            end_button = Button(text="End Quizlet Window",command= self.end_app, highlightthickness=0)
            end_button.grid(row=2,column=0)
            

