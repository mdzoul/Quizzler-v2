"""This is the code for how the quiz is run"""
import html


class QuizBrain:
    """This runs at the backend for how the quiz is to be run"""

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        """Output True only if there are still questions unanswered"""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Outputs the text for the next question"""
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        question_text = html.unescape(self.current_question.text)
        return question_text

    def check_answer(self, user_answer):
        """Outputs True or False based on user's input"""
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
