"""This simple code sets how the question should model"""


class Question:
    """Models the question"""

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
