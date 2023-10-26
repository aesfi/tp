class Question:
    def __init__(self, question, options, correct_answer):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer
        self.user_answer = None

    def is_correct(self):
        return self.user_answer and self.user_answer.lower() == self.correct_answer

    def get_question(self):
        return self.question

    def get_options(self):
        return self.options