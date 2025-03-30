# bill calculator by using getters and setters

class Bill:
    def __init__(self,item_no,items,total_items,price_of_unit):
        self.sr_no=item_no
        self.description=items
        self.quantity=total_items
        self.unit_price=price_of_unit

    @property
    def sr_no(self):
        return self.item_no
    @sr_no.setter
    def sr_no(self,d):
        self.item_no=d
        return
    
    @property
    def description(self):
        return self.items
    @description.setter
    def description(self,d):
        self.items=d
        return
    
    @property
    def quantity(self):
        return self.total_items
    @quantity.setter
    def quantity(self,d):
        self.total_items=d
        return
    
    @property
    def unit_price(self):
        return self.price_of_unit
    @unit_price.setter
    def unit_price(self,d):
        self.price_of_unit=d
        return
    
    def print_details(self):
        print(self.sr_no)
        print(self.description)
        print(self.quantity)
        print(self.unit_price)

def main():
    a=input("Enter Item No ")
    b=input("Enter item name ")
    c=input("Enter item quantity ")
    d=input("Enter price of unit ")

    bill1=Bill(a,b,c,d)
    bill1.print_details()

main()
