import random
from random import randint
import dill


class Quiz:
    question_num: int = random.randint(0, 10)

    def __init__(self):
        pass

    def questions(self):
        with open(f'questions/question{Quiz.question_num}.txt', 'r') as f:
            question = f.readlines()
        return question

    def answers(self):
        with open(f'answers/answer{Quiz.question_num}.txt', 'r') as f:
            answer = f.readlines()
        return answer


class TrueFalse(Quiz):
    pass


class MultipleChoice(Quiz):
    pass


class ShortAnswers(Quiz):
    pass


class Points:
    point: int

    @classmethod
    def save_points(cls):
        if True:
            Points.point += 10
        elif None:
            Points.point = Points.point
        else:
            Points.point -= 3

    @classmethod
    def check_win(cls):
        if