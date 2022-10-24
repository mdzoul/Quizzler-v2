"""This is the main code to run"""
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizUI

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizUI(quiz)

print("You've completed the quiz!")
if quiz.score == quiz.question_number:
    print(f"Your final score: {quiz.score}/{quiz.question_number}")
else:
    print(f"Your final score: {quiz.score}/{quiz.question_number}")
