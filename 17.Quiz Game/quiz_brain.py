
# question_number = 0
# question_list = 0
class QuizBrain:

    def __init__(self,q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.answer = None

    def next_question(self):
        current_question = self.question_list[self.question_number].text
        self.question_number += 1
        self.answer = input(f"Q.{self.question_number}: {current_question} (True/False)")

    def still_has_questions(self):
        return len(self.question_list) > self.question_number

    def check_answer(self):
        
        if self.answer == self.question_list[self.question_number-1].answer:
            self.score += 1
            print("Correct Answer.")
        else:
            print("Wrong Answer")
                
