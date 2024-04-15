from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for element in question_data:
    # print(element.get("text"))
    # print(element.get("answer"))
    question_bank.append(Question(element["text"], element["answer"]))

# print(question_bank[0].text)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the Quiz!")
print(f"Your final score was {quiz.score} out of {quiz.question_number}!")
