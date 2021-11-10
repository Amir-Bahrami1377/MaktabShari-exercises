import pickle


multiple_choice = [
    {
        "question_type": "multiple_choice",
        "question": "111 + 111 = ?",
        "options": ["1)425", "2)222", "3)333", "4)321"],
        "answer": "2"
    },
    {
        "question_type": "multiple_choice",
        "question": "3 * 5 = ?",
        "options": ["1)10", "2)50", "3)15", "4)20"],
        "answer": "3"
    },
    {
        "question_type": "multiple_choice",
        "question": "121 + 212 = ?",
        "options": ["1)425", "2)343", "3)321", "4)333"],
        "answer": "4"
    }
]

true_false = [
    {
        "question_type": "true_false",
        "question": "2 + 3 is 5 ?",
        "answer": "true"
    },
    {
        "question_type": "true_false",
        "question": "Snow is black",
        "answer": "false"
    },
    {
        "question_type": "true_false",
        "question": "Sun is blue",
        "answer": "false"
    },
    {
        "question_type": "true_false",
        "question": "366 + 857 is 1127 ?",
        "answer": "false"
    },
    {
        "question_type": "true_false",
        "question": "245 + 817 is 1162 ?",
        "answer": "false"
    },
    {
        "question_type": "true_false",
        "question": "Mr.Tehrani is lovely",
        "answer": "true"
    },
    {
        "question_type": "true_false",
        "question": "1kg wool is heavier than 1kg Iron",
        "answer": "false"
    }
]

short_answer = [
    {
        "question_type": "short_answer",
        "question": "Capital of Iran",
        "answer": "Tehran"
    },
    {
        "question_type": "short_answer",
        "question": "Capital of Germany",
        "answer": "Berlin"
    },
    {
        "question_type": "short_answer",
        "question": "Capital of Taiwan",
        "answer": "Taipei"
    },
    {
        "question_type": "short_answer",
        "question": "4 + 6 is ?",
        "answer": "10"
    },
    {
        "question_type": "short_answer",
        "question": "32 * 8 is ?",
        "answer": "256"
    },
    {
        "question_type": "short_answer",
        "question": "24 * 11 is ?",
        "answer": "264"
    }
]

tests = [*multiple_choice, *true_false, *short_answer]


def save_pickle():
    with open('questions.pk', "wb") as f:
        pickle.dump(tests, f)


save_pickle()