# write a program to simplify a fraction

class simplify_fraction:
    simplified_numerator=0
    simplified_denominator=0

    def __init__(self,numerator,denominator):
        self.numerator=numerator
        self.denominator=denominator

    def print_fraction(self):
        print(f"The given fraction is {self.numerator}/{self.denominator}")

    def calculate_simplified_fraction(self):
        if self.denominator>self.numerator:
            self.n=self.denominator
        if self.numerator>self.denominator:
            self.n=self.numerator

        for i in range(2,self.n):
            if self.numerator%i==0 and self.denominator%i==0:
                self.simplified_numerator=self.numerator//i
                self.simplified_denominator=self.denominator//i
            if self.simplified_numerator<self.numerator:
                self.final_numerator=self.simplified_numerator
            if self.simplified_denominator<self.denominator:
                self.final_denoninator=self.simplified_denominator
        
        if self.final_numerator==0 and self.final_denoninator==0:
            self.final_numerator=self.numerator
            self.final_deniminator=self.denominator
      
    def print_simplified_fraction(self):
        print(f"The simplified fraction is {self.final_numerator}/{self.final_denoninator}")

def main():
    f=simplify_fraction(1000,20)
    f.print_fraction()
    f.calculate_simplified_fraction()
    f.print_simplified_fraction()
main()

