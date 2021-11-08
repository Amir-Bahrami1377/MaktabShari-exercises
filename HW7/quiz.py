from random import randint
import pickle
from models import Quiz


def load_pickle():
    with open('questions.pk', 'rb') as f:
        return pickle.load(f)


random_number = randint(0, 2)
question_series: list = load_pickle()
question_lists: list = question_series[random_number]


def data_set():
    question = question_lists.pop(0)
    new_obj = Quiz(question[0], question[1])
    return new_obj


available_obj = data_set()

