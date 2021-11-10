import pickle
import random

from models import Quiz, Score, User


questions_count = 6
def load_pickle():
    """
    loads pickled questions
    """
    with open('questions.pk', 'rb') as f:
        return pickle.load(f)


def create_random_questions(data):
    questions = []
    for i in range(questions_count):
        question = random.choice(data)
        questions.append(question)
        data.remove(question)
    return questions


def ask_question(question, i):
    options = None
    if question.question_type == "multiple_choice":
        options = "[1, 2, 3, 4]"
    elif question.question_type == "true_false":
        options = "[true, false]"
    elif question.question_type == "short_answer":
        options = "write down the correct answer"
    return f"Question {i+1}:\n{question.__call__()}\nOptions: {options}\n"


def starting_menu(user: User = None):
    get_question = (question for question in create_random_questions(load_pickle()))
    score = Score()
    if not user:
        username = input("Please enter your name: \n")
        user = User(username)
    user.score = score
    for i in range(questions_count):
        quiz = Quiz(**next(get_question))
        answer = input(ask_question(quiz, i))
        if not answer:
            user.score.not_answered += 1
        else:
            if quiz.check_answer(answer):
                user.score.add_points()
                print("True :D")
            else:
                user.score.minus_point()
                print("False :(")
        print(f"current score: {user.score.points}\n##########\n")
    if user.score.check_point():
        print("hooray you are the winner !!!")
        print(user.__str__())
    else:
        print("sorry but you lost ...")
        print(user.__str__())
    return user