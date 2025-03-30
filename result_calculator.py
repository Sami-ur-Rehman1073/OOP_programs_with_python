# Write a program which takes marks of the subjects of the student and gives
# total and percentage of the subjects

class result:
    def __init__(self,e,u,m,s,i,p):
        self.English=e
        self.Urdu=u
        self.Math=m
        self.Science=s
        self.Islamiyat=i
        self.Pakistan_studies=p

    def print_marks(self):
        print(f"Marks in English: {self.English}/100")
        print(f"Marks in Urdu: {self.Urdu}/100")
        print(f"Marks in Math: {self.Math}/100")
        print(f"Marks in Science: {self.Science}/100")
        print(f"Marks in Islamiyat: {self.Islamiyat}/100")
        print(f"Marks in Pakistan Studies: {self.Pakistan_studies}/100")
    
    def calculate_result(self):
        self.total_marks=600
        self.obtained_marks=self.English+self.Urdu+self.Math+self.Science+self.Islamiyat+self.Pakistan_studies
        self.percentage=(self.obtained_marks/self.total_marks)*100
    
    def print_result(self):
        print(f"The student has obtained {self.obtained_marks} marks from {self.total_marks}")
        print(f"The student has got {self.percentage} marks")

def main():
    c1=result(72,65,74,96,56,78)
    c1.print_marks()
    c1.calculate_result()
    c1.print_result()
main()
