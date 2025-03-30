# write a program to take a test from a student and then give total marks 
# at the end

from random import *

class questions:

    total_marks=0

    def __init__(self):
        self.first_value=randint(1,10)
        self.second_value=randint(1,10)
        self.operation=randint(1,4)
    
    def print_question(self):
        if self.operation==1:
            print(f"{self.first_value}+{self.second_value}=")
        if self.operation==2:
            print(f"{self.first_value}-{self.second_value}=")
        if self.operation==3:
            print(f"{self.first_value}x{self.second_value}=")
        if self.operation==4:
            print(f"{self.first_value}/{self.second_value}=")
    
    def input_answer(self):
        self.answer=int(input("Enter The answer  "))
    
    def calculate_answer(self):
        if self.operation==1:
            self.correct_answer=self.first_value+self.second_value
        if self.operation==2:
            self.correct_answer=self.first_value-self.second_value
        if self.operation==3:
            self.correct_answer=self.first_value*self.second_value
        if self.operation==4:
            self.correct_answer=self.first_value/self.second_value

    def print_answer(self):
        if self.answer==self.correct_answer:
            print("The answer is correct")
        else:
            print("Wrong Answer!")
            print(f"The correct answer is {self.correct_answer}")
    
    def marks_calculator(self):
        if self.answer==self.correct_answer:
            self.total_marks+=1
        if self.answer!=self.correct_answer:
            self.total_marks+=0
    
    def print_total_marks(self):
        print(f"You obtained {self.total_marks} marks")

def main():
    for i in range(3):
        q1=questions()
        q1.print_question()
        q1.input_answer()
        q1.calculate_answer()
        q1.print_answer()
        q1.marks_calculator()
        q1.print_total_marks()
main()