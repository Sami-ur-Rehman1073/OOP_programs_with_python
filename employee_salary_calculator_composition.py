# write a program to calculate the salary of an employee by composition 

class Salary:
    def __init__(self,salary,bonus,tax):
        self.employee_salary=salary
        self.employee_bonus=bonus
        self.employee_tax=tax

    def salary_calculator(self):
        self.total_salary=self.employee_salary+self.employee_bonus-(self.employee_tax/100)
class Employee:
    def __init__(self,name,age,post,salary,bonus,tax):
        self.employee_name=name
        self.employee_age=age
        self.employee_post=post
        self.employee_salary=salary
        self.employee_bonus=bonus
        self.employee_tax=tax
        self.obj_salary=Salary(salary,bonus,tax)

    def calculate_salary(self):
        self.obj_salary.salary_calculator()
        print(self.obj_salary.total_salary)

def main():
    emp=Employee("Sami",19,"Software Dveloper",900000,25000,10)
    emp.calculate_salary()
main()

    