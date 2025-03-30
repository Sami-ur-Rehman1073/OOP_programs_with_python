# write a program to calculate a bill.

class bill:
    def __init__(self,sr_no,item_name,quantity,unit_price):
        self.sr_no=sr_no
        self.item_name=item_name
        self.quantity=quantity
        self.unit_price=unit_price
        self.total_price=self.unit_price*self.quantity
    
    def __str__(self):
        s=str(self.sr_no)+ self.item_name + str(self.quantity) + str(self.unit_price) + str(self.total_price)
        return s
    
def main():
    list=[]
    total_bill=0
    for i in range(1,3):
        a=i
        b=str(input("Enter the name of the item  "))   
        c=int(input("Enter the quantity of the item  "))   
        d=int(input("Enter the unit price of the item  "))   
        order=bill(a,b,c,d)
        print(order)
        list.append(order.total_price)
    for j in range(len(list)):
        total_bill+=list[j]
    print(f"Your total bill is {total_bill}")

main()