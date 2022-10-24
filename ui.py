"""This is the code for the UI"""
from tkinter import Tk, Canvas, Label, Button, PhotoImage
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
TRUE_COLOR = "#2bb677"
FALSE_COLOR = "#ef665d"
FONT = ("Arial", 20, "italic")


class QuizUI:
    """The Quiz User Interface"""

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler v2")
        self.window.config(padx=20, pady=40, bg=THEME_COLOR)

        # Canvas
        self.canvas = Canvas(width=500, height=250, bg="white", highlightthickness=0)
        self.canvas.grid(row=2, column=1, columnspan=2, pady=40)

        self.question_num = self.canvas.create_text(
            70, 30,
            text="Q",
            font=("Arial", 20, "bold"),
            fill=THEME_COLOR,
        )
        self.question_text = self.canvas.create_text(
            250, 125,
            width=400,
            text="",
            font=FONT,
            fill=THEME_COLOR,
        )
        self.score_text = self.canvas.create_text(
            440, 30,
            text=f"Score: {self.quiz.score} / {self.quiz.question_number}",
            font=("Arial", 15, "bold"),
            fill=THEME_COLOR,
        )

        # Title Label
        self.title_label = Label(
            text="Quizzler v2",
            fg="white",
            bg=THEME_COLOR,
            font=("Arial", 40, "bold")
        )
        self.title_label.grid(row=1, column=1, columnspan=2)

        # Buttons (True/False)
        true_img = PhotoImage(file="./images/true.png")
        self.true_btn = Button(
            image=true_img,
            highlightbackground=THEME_COLOR,
            command=self.click_true
        )
        self.true_btn.grid(row=3, column=1)

        false_img = PhotoImage(file="./images/false.png")
        self.false_btn = Button(
            image=false_img,
            highlightbackground=THEME_COLOR,
            command=self.click_false
        )
        self.false_btn.grid(row=3, column=2)

        self.next_qn()

        self.window.mainloop()

    def next_qn(self):
        """Pulls out the next question from QuizBrain class"""
        self.canvas.config(bg="white")
        self.canvas.itemconfig(self.score_text, text=f"Score: {self.quiz.score} / {self.quiz.question_number}")

        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_num, text=f"Question {self.quiz.question_number}")
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.title_label.config(
                text=f"Your final score: {self.quiz.score} / {self.quiz.question_number}",
            )
            self.canvas.itemconfig(
                self.question_text,
                text=f"You've completed the quiz!"
            )
            # self.canvas.create_text(
            #     250, 150,
            #     text="Click X to exit",
            #     font=FONT,
            #     fill=THEME_COLOR,
            # )
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def click_true(self):
        """Method for when True button is pressed"""
        self.feedback(self.quiz.check_answer("True"))

    def click_false(self):
        """Method for when False button is pressed"""
        self.feedback(self.quiz.check_answer("False"))

    def feedback(self, is_correct):
        """Gives color feedback based on whether user guess is correct or not"""
        if is_correct:
            self.canvas.config(bg=TRUE_COLOR)
        else:
            self.canvas.config(bg=FALSE_COLOR)

        self.window.after(1000, self.next_qn)
