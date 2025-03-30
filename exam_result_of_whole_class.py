# write a program to calculate the result of a class.

from random import *
class marks:
    total_marks=600

    def __init__(self,name_of_student,english,urdu,maths,science,islamiat,pst):
        self.name=name_of_student
        self.marks_in_english=english
        self.marks_in_urdu=urdu
        self.marks_in_math=maths
        self.marks_in_science=science
        self.marks_in_islamiat=islamiat
        self.marks_in_pakstudies=pst

    @property
    def name(self):
        return self.name_of_student
    @name.setter
    def name(self,d):
        self.name_of_student=d
        return
    
    @property
    def marks_in_english(self):
        return self.english
    @marks_in_english.setter
    def marks_in_english(self,d):
        self.english=d
        return
    
    @property
    def marks_in_urdu(self):
        return self.urdu
    @marks_in_urdu.setter
    def marks_in_urdu(self,d):
        self.urdu=d

    @property
    def marks_in_math(self):
        return self.maths
    @marks_in_math.setter
    def marks_in_math(self,d):
        self.maths=d
        return
    
    @property
    def marks_in_science(self):
        return self.science
    @marks_in_science.setter
    def marks_in_science(self,d):
        self.science=d
        return
    
    @property
    def marks_in_islamiat(self):
        return self.islamiat
    @marks_in_islamiat.setter
    def marks_in_islamiat(self,d):
        self.islamiat=d
        return
    
    @property
    def marks_in_pakstudies(self):
        return self.pst
    @marks_in_pakstudies.setter
    def marks_in_pakstudies(self,d):
        self.pst=d
        return

class calculate_result:
    data2=[]
    @staticmethod
    def result_calculator(data):
        for i in range(len(data)):
           data[i].obtained_marks=data[i].marks_in_english+data[i].marks_in_urdu+data[i].marks_in_math+data[i].marks_in_science+data[i].marks_in_islamiat+data[i].marks_in_pakstudies
           data[i].percent_obtained=(data[i].obtained_marks/data[i].total_marks)*100
           calculate_result.data2.append(data[i])


class display_result:
    @staticmethod
    def show_result(l):
        for i in range(len(l)):
            print(f"Student Name: ",l[i].name)
            print(f"Marks in English: ",l[i].marks_in_english)
            print(f"Marks in Urdu: ",l[i].marks_in_urdu)
            print(f"Marks in Mathematics: ",l[i].marks_in_math)
            print(f"Marks in Science: ",l[i].marks_in_science)
            print(f"Marks in Islamiat: ",l[i].marks_in_islamiat)
            print(f"Marks in Pak Studies: ",l[i].marks_in_pakstudies)
            print(f"Obtained Marks: ",l[i].obtained_marks)
            print(f"Total Marks: ",l[i].total_marks)
            print(f"Percentage: ",l[i].percent_obtained)
            print()
            

def main():     
    data=[]
    for i in range(2):
        name=input("Enter the name of the student:  ")
        eng=randint(1,100)
        urd=randint(1,100)
        math=randint(1,100)
        sci=randint(1,100)
        isl=randint(1,100)
        pst=randint(1,100)
        student=marks(name,eng,urd,math,sci,isl,pst)
        data.append(student)
    calculate_result.result_calculator(data)
    display_result.show_result(calculate_result.data2)
    max=0
    for i in range(len(calculate_result.data2)):
        if calculate_result.data2[i].obtained_marks>max:
            max=calculate_result.data2[i].obtained_marks
            obj=calculate_result.data2[i]

main()