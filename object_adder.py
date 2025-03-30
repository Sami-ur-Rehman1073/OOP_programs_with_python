# write a program to add lists of two objects.
class object:
    def __init__(self,x):
        self.x=x
    def add_x(a,b):
        r=a.x+b.x
        return r

def main():
    a=object(2)
    b=object(3)
    print(a.add_x(b))
main()