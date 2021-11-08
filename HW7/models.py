from exceptions import UserError

class Quiz:

    def __init__(self, question: str, answer: str):
        self.question = question
        self.answer = answer

    def questions(self):
        return self.question

    def check_answer(self, input_answer: str):
        if self.answer != input_answer.lower():
            return False
        return True


class TrueFalse(Quiz):

    def __init__(self):
        super().__init__()

    def questions(self):
        super().questions()

    def check_answer(self, input_answer):
        super().check_answer()


class ShortAnswer(Quiz):

    def __init__(self):
        super().__init__()

    def questions(self):
        super().questions()

    def check_answer(self, input_answer):
        super().check_answer()


class MultipleChoice(Quiz):

    def __init__(self):
        super().__init__()

    def question(self):
        super().questions()

    def check_answer(self, input_answer: str):
        super().check_answer()


class Point:
    corrects: int
    wrongs: int
    not_answered: int
    points: int

    @classmethod
    def add_points(cls):
        Point.points += 10
        Point.corrects += 1
        return Point.points

    @classmethod
    def minus_point(cls):
        Point.points -= 3
        Point.wrongs += 1
        return Point.points

    @classmethod
    def check_point(cls):
        if Point.points < 40:
            return False
        return True


class User:

    def __init__(self, name):
        self.__check_data(name)
        self.name = name

    def __check_data(self, name):
        if len(name) < 1:
            raise UserError("name can't be empty", 'name', name)

    def __str__(self):
        return f"live result {self.name} => correct answers: {Point.corrects} && wrong answers: {Point.wrongs} && Noun answers: {Point.not_answered} "