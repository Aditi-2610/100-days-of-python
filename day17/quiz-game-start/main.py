from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for i in question_data:
    # my_question1 = Question(i["text"], i["answer"])
    my_question = Question(i["question"], i["correct_answer"])
    question_bank.append(my_question)


# print(question_bank[0].answer)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print("You've completed the quiz!")
print(f"Your final score is: {quiz.user_score}/{quiz.question_number}.")

