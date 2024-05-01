from question_model import Question
from main import question_data
from quiz_brain import QuizBrain


question_bank = []
for element in question_data:
    question_bank.append(Question(element["question"], element["correct_answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the Quiz!")
print(f"Your final score was {quiz.score} out of {quiz.question_number}!")
