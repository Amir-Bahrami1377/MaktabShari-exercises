import pickle

questions = [
    [["true false: 2 + 3 = 5", "true"], ["4 + 6 = ", "10"], ["Capital of Iran?", "tehran"], ["3 * 5= \n 1)10 \t 2)50 \n 3)15 \t 4)20", "3"], ["1kg wool is heavier than 1kg Iron(true,false)", "false"]],
    [["true false: 366 + 857 = 1127", "false"], ["32 * 8= ", "256"], ["Capital of Germany?", "berlin"], ["111 + 111 = \n 1)131 \t 2)121 \n 3)212 \t 4)321", "2"], ["Mr.Tehrani is lovely(true,false)", "true"]],
    [["true false: 245 + 817 = 1162", "false"], ["24 * 11= ", "264"], ["Capital of Taiwan?", "taipei"], ["121 + 212 = \n 1)425 \t 2)343 \n 3)333 \t 4)321", "3"], ["Mr.Yazdani is older than Mr.Tehrani(true,false)", "false"]]

]


def save_pickle():
    with open('questions.pk', "wb") as f:
        pickle.dump(questions, f)


save_pickle()
