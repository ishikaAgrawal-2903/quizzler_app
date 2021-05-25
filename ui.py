from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
END_COLOR = "#bbf1fa"


class QUizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text=f"Score: 0", bg=THEME_COLOR, fg="white", font=("Courier", 11, "bold"))
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(width=320, height=250, bg="white")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.question_text = self.canvas.create_text(
            160,
            110,
            text="Some question text",
            width=320,
            fill=THEME_COLOR,
            font=("Arial", 18, "italic")
        )

        right_image = PhotoImage(file="images/true.png")
        self.right_button = Button(image=right_image, highlightthickness=0, bg=THEME_COLOR, command=self.true_pressed)
        self.right_button.grid(column=0, row=2)

        wrong_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong_image, highlightthickness=0, bg=THEME_COLOR, command=self.false_pressed)
        self.wrong_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,
                                   text=f"You have reached at the end of the quiz.\nYour score: {self.quiz.score}")
            self.canvas.config(bg=END_COLOR)
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")
    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.get_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.get_feedback(is_right)

    def get_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else :
            self.canvas.config(bg="red")
        self.window.after(1000,  self.get_next_question)




