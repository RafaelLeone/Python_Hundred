from question_model import Question
from data import question_data


question_bank = []
for element in question_data:
    # print(element.get("text"))
    # print(element.get("answer"))
    question_bank.append(Question(element["text"], element["answer"]))

# print(question_bank[0].text)
