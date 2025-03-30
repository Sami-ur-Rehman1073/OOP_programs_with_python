# inheritence

class Student:

    def __init__(self,name,grade,section):
        self.student_name=name 
        self.student_grade=grade
        self.section=section
    
    def __str__(self):
        v=f"The student name is {self.student_name}"
        return v
    
    def print_grade(self):
        print(f"The student studies is {self.student_grade}")

class result(Student):
    def __init__(self,name,grade,section,obtained_marks,total_marks,percent):
        super().__init__(name,grade,section)
        self.student_obtained_marks=obtained_marks
        self.student_total_marks=total_marks
        self.student_percent=percent

    def __str__(self):
        return super().__str__()
    
    def grade_printer(self):
        super().print_grade()
        
def main():
    r=result("Sami","Nine","C",500,600,90)
    print(r)
    r.grade_printer()
main()