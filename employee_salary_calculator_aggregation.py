# program of aggregation

class Salary:
    def __init__(self,salary,bonus,tax):
        self.employee_salary=salary
        self.employee_bonus=bonus
        self.employee_tax=tax

    def salary_calculator(self):
        self.total_salary=self.employee_salary+self.employee_bonus-((self.employee_tax/100)*self.employee_salary)
class Employee:
    def __init__(self,name,age,post,sal):
        self.employee_name=name
        self.employee_age=age
        self.employee_post=post
        self.obj_salary=sal

    def calculate_salary(self):
        self.obj_salary.salary_calculator()
        print(self.obj_salary.total_salary)

def main():
    sal=Salary(10000,100,10)
    emp=Employee("Sami",19,"Software Dveloper",sal)
    emp.calculate_salary()
main()