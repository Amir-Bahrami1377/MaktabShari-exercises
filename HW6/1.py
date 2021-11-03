
numbers_dict = {'one': "1", 'two': "2", 'three': "3", 'four': "4", 'five': "5", 'six': "6", 'seven': "7", 'eight': "8", 'nine': "9", 'ten': "10", 'eleven': "11", 'twelve': "12", 'thirteen': "13", 'fourteen': "14", 'fifteen': "15", 'sixteen': "16", 'seventeen': "17", 'eighteen': "18", 'nineteen': "19", 'twenty': "20"}


file = open('input-q-1.txt', 'r')
content = file.read()
file.close()
splited_content = content.split(' ')

for target in splited_content:
    if target in numbers_dict.keys():
        position = int(splited_content.index(target))
        splited_content.pop(position)
        splited_content.insert(position, numbers_dict.get(target))

content = " ".join(splited_content)

with open('output-q-1.txt', 'w') as f:
    f.write(content)
