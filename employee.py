class Employee:

    def __init__(self,employee_no,name_of_employee,cnic_no,phone,residence):
        self.employee_number=employee_no
        self.employee_name=name_of_employee
        self.cnic=cnic_no
        self.contact_no=phone
        self.address=residence

class Salaried_employee(Employee):

    def __init__(self,employee_no,name_of_employee,cnic_no,phone,residence,week_salary):
        super().__init__(employee_no,name_of_employee,cnic_no,phone,residence)
        self.weekly_salary=week_salary
  
    def info_and_salary(self):
        print(f"Employee Number: {self.employee_number}")
        print(f"Employee Name: {self.employee_name}")
        print(f"Employee CNIC: {self.cnic}")
        print(f"Employee CNIC: {self.cnic}")
        print(f"Employee Phone: {self.contact_no}")
        print(f"Employee Address: {self.address}")
        print(f"Employee Salary: {self.weekly_salary}")

class Hourly_employee(Employee):

    def __init__(self,employee_no,name_of_employee,cnic_no,phone,residence,hours,rate):
        super().__init__(employee_no,name_of_employee,cnic_no,phone,residence)
        self.work_hours=hours
        self.rate_per_hour=rate

    def calculate_pay(self):
        self.hours_salary=self.work_hours*self.rate_per_hour

    def info_and_salary(self):
        print(f"Employee Number: {self.employee_number}")
        print(f"Employee Name: {self.employee_name}")
        print(f"Employee CNIC: {self.cnic}")
        print(f"Employee CNIC: {self.cnic}")
        print(f"Employee Phone: {self.contact_no}")
        print(f"Employee Address: {self.address}")
        print(f"Employee Salary: {self.hours_salary}")

class Comisssion_employee(Employee):

    def __init__(self,employee_no,name_of_employee,cnic_no,phone,residence,sales,share):
        super().__init__(employee_no,name_of_employee,cnic_no,phone,residence)
        self.company_sales=sales
        self.percentage=share
    
    def calculate_pay(self):
        self.percent=self.percentage/100
        self.comission_salary=self.company_sales*self.percent

    def info_and_salary(self):
        print(f"Employee Number: {self.employee_number}")
        print(f"Employee Name: {self.employee_name}")
        print(f"Employee CNIC: {self.cnic}")
        print(f"Employee CNIC: {self.cnic}")
        print(f"Employee Phone: {self.contact_no}")
        print(f"Employee Address: {self.address}")
        print(f"Employee Salary: {self.comission_salary}")

def main():
    a1=Salaried_employee("1","Sami","1234","0334","Lahore",15000)
    a2=Hourly_employee("2","Ahmad","3453","0323","Lahore",40,150)
    a3=Comisssion_employee("3","Butt","1394","0343","Lahore",400000,10)
    a2.calculate_pay()
    a3.calculate_pay()
    print()
    a1.info_and_salary()
    print()
    a2.info_and_salary()
    print()
    a3.info_and_salary()
    print()

main()