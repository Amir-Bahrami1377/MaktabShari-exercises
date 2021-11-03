import re


with open('input-q-2.txt', 'r') as f:
    content = f.read()


"""
this function will use splited text to find words
ending with '.' and  it will save their index number
in a list then they will be used to make sentences
and sentences will be save in a file
"""


def part_one(content):
    splited_content = content.split(" ")
    positions = []
    content2 = []

    for word in splited_content:
        if word.endswith("."):
            positions.append(splited_content.index(word))

    poped: int = -1
    for position in positions:
        end_line = position - poped
        for poping in range(end_line):
            content2.append(splited_content.pop(0))
        poped += end_line
        sentence = " ".join(content2)
        with open('output-q-2-1.txt', 'a') as f:
            f.write(f" {sentence} \n")
        content2.clear()


def part_two(content):
    content2 = re.sub("\n", " ", content)
    print(content2)
    uniq_list = list(set(content2.split(" ")))
    uniqs = " - ".join(uniq_list)
    with open('output-q-2-2.txt', 'w') as f:
        f.write(f"{uniqs}")


#part_one(content)
part_two(content)