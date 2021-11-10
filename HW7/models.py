from typing import NoReturn

from exceptions import UserError


class Quiz:
    def __init__(self, question, answer, options=None, question_type=None) -> NoReturn:
        self.question = question
        self.answer = answer
        self.options = options
        self.question_type = question_type

    def __call__(self) -> str:
        if self.options:
            return f"{self.question}\n{' '.join(self.options)}"
        return self.question

    def check_answer(self, user_answer) -> bool:
        if self.answer.lower() != user_answer.lower():
            return False
        return True


class TrueFalse(Quiz):
    pass


class ShortAnswer(Quiz):
    pass


class MultipleChoice(Quiz):
    pass


class Score:
    def __init__(self):
        self.corrects = 0
        self.wrongs = 0
        self.not_answered = 0
        self.points = 0

    def add_points(self):
        self.points += 10
        self.corrects += 1
        return self.points

    def minus_point(self):
        self.points -= 3
        self.wrongs += 1
        return self.points

    def check_point(self):
        if self.points < 40:
            return False
        return True


class User:
    def __init__(self, name, score: Score = None):
        self.__check_data(name)
        self.name = name
        self.score = score

    def __check_data(self, name):
        if len(name) < 1:
            raise UserError("name can't be empty", 'name', name)

    def __str__(self):
        return f"live result {self.name} => correct answers: {self.score.corrects}" \
               f" && wrong answers: {self.score.wrongs} && Noun answers: {self.score.not_answered}"