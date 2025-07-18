class Question:
    def __init__(self, ques, ans):
        self.ques = ques
        self.ans = ans

class QuizBrain:
    def __init__(self, q_list):
        self.q_no = 0
        self.q_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.q_no < len(self.q_list)

    def nextQuestion(self):
        current_question = self.q_list[self.q_no]
        self.q_no += 1
        user_answer = input(f"Q{self.q_no}: {current_question.ques}(True/False): ")
        self.check_answer(user_answer, current_question.ans)
        print(f"Your current score is: {self.score}/{self.q_no}")

    def check_answer(self, user_answer, correct_answer):
        if user_answer.title() == correct_answer:
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong!")
        print(f"The correct answer is {correct_answer}")


Q1 = Question("The capital of Australia is Sydney. ", "False")
Q2 = Question("The Great Wall of China is visible from space. ", "False")
Q3 = Question("The human body has 206 bones. ", "True")
Q4 = Question("Mount Everest is the tallest mountain in the world. ", "True")

Question_Bank = [Q1, Q2, Q3, Q4]
Quiz = QuizBrain(Question_Bank)

while Quiz.still_has_questions():
    Quiz.nextQuestion()

print("\nYou've completed the quiz!")
print(f"Your final score is: {Quiz.score}/{Quiz.q_no} ")