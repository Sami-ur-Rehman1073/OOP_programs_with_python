class Department:
    
    def __init__(self,short_name,name,chairman):
        self.department_short_name=short_name
        self.department_name=name
        self.department_chairman=chairman

    @property
    def department_short_name(self):
        return self.short_name
    @department_short_name.setter
    def department_short_name(self,d):
        self.short_name=d
        return
    @property
    def department_name(self):
        return self.name
    @department_name.setter
    def department_name(self,d):
        self.name=d
        return
    @property
    def department_chairman(self):
        return self.chairman
    @department_chairman.setter
    def department_chairman(self,d):
        self.chairman=d
        return

    def display_department_information(self):
        print("Department:",end="      ")
        print(self.department_short_name,end="      ")
        print(self.department_name,end="     ")
        print(self.department_chairman,end="    ")


class Student:
    
    def __init__(self,department,roll_no,name,semester,gpa):
        self.student_department=department
        self.student_roll_no=roll_no
        self.student_name=name
        self.student_semester=semester
        self.student_gpa=gpa

    @property
    def student_department(self):
        return self.department
    @student_department.setter
    def student_department(self,d):
        self.department=d
        return
    @property
    def student_roll_no(self):
        return self.roll_no
    @student_roll_no.setter
    def student_roll_no(self,d):
        self.roll_no=d
        return
    @property
    def student_name(self):
        return self.name
    @student_name.setter
    def student_name(self,d):
        self.name=d
        return
    @property
    def student_semester(self):
        return self.semester
    @student_semester.setter
    def student_semester(self,d):
        self.semester=d
        return
    @property
    def student_gpa(self):
        return self.gpa
    @student_gpa.setter
    def student_gpa(self,d):
        self.gpa=d
        return

    def display_student_information(self):
        print("Student Roll No:",self.student_roll_no,end="      ")
        print("Student Name:",self.student_name,end="      ")
        print("Student Semester:",self.student_semester,end="      ")
        print("Student GPA:",self.student_gpa,end="      ")

def main():
    CS=[]
    SE=[]
    IT=[]
    DS=[]
    less_gpa=[]
    s=Student("IT","1","Sami","2","2.65")
    s=Student("DS","18","Sami","2","1.50")
    if s.student_department=="CS":
        CS.append(s)
    if s.student_department=="SE":
        SE.append(s)
    if s.student_department=="IT":
        IT.append(s)
    if s.student_department=="DS":
        DS.append(s)

    d1=Department("CS","Computer Science","Dr.Jodat Kamal")
    d1.display_department_information()
    print()
    if CS==[]:
        print("No Data")
    else:
        for i in range(len(CS)):
            CS[i].display_student_information()
    print()
            
    d2=Department("SE","Software Engineering","Dr.Asif Iqbal")
    d2.display_department_information()
    print()
    if SE==[]:
        print("No Data")
    else:
        for i in range(len(SE)):
            SE[i].display_student_information()
    print()
            
    d3=Department("IT","Information Technology","Dr.Mustafa Ali")
    d3.display_department_information()
    print()
    if IT==[]:
        print("No Data")
    else:
        for i in range(len(IT)):
            IT[i].display_student_information()
    print()

    d4=Department("DS","Data Science","Dr.Rehman Ali")
    d4.display_department_information()
    print()
    if DS==[]:
        print("No Data")
    else:
        for i in range(len(DS)):
            DS[i].display_student_information()
    print()
    
    print("The students with GPA less than 1.70 are")
    if CS!=[]:
        for i in range(len(CS)):
            p=float(CS[i].student_gpa)
            if p<1.70:
                less_gpa.append(CS[i])
    
    if SE!=[]:
        for i in range(len(SE)):
            p=float(SE[i].student_gpa)
            if p<1.70:
               if p<1.70:
                less_gpa.append(CS[i])

    if IT!=[]:
        for i in range(len(IT)):
            p=float(IT[i].student_gpa)
            if p<1.70:
               if p<1.70:
                less_gpa.append(IT[i])

    if DS!=[]:
        for i in range(len(DS)):
            p=float(DS[i].student_gpa)
            if p<1.70:
               if p<1.70:
                less_gpa.append(DS[i])

    for i in range(len(less_gpa)):
        less_gpa[i].display_student_information()
           
main()

        
