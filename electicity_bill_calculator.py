# write a program that calculates the total electricity bill if units
#  consumed is provided as an input

class electricity_bill:
    unit_price=50
    def __init__(self,units=0):
        self.units=units

    def calculate_bill(self):
        self.total_bill_price=self.unit_price*self.units
    
    def print_bill(self):
        print(f"Your total bill is {self.total_bill_price}")

def main():
    customer1=electricity_bill(300)
    customer1.calculate_bill()
    customer1.print_bill()
main()