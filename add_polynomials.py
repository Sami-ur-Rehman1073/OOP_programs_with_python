# write a program to add two polynomials

class polynomial:
    polynomial_list=[]

    def __init__(self,v5=0,v4=0,v3=0,v2=0,v1=0,string="None"):
        self.cofficient_list=[]
        self.c5=v5
        self.c4=v4
        self.c3=v3
        self.c2=v2
        self.c1=v1
        self.string=string

    def create_cofficient_list(self):
        self.cofficient_list.append(self.c5)
        self.cofficient_list.append(self.c4)
        self.cofficient_list.append(self.c3)
        self.cofficient_list.append(self.c2)
        self.cofficient_list.append(self.c1)
    
    # def print_cofficient_list(self):
    #     print(self.cofficient_list)

    def create_polynomial(self):
        i=5
        self.list=[]
        for j in range(len(self.cofficient_list)):
            term=str(self.cofficient_list[j])+self.string+str(i)
            self.list.append(term)
            i=i-1
        # print(self.list)

    def print_polynomial(self):
        pol=""
        for k in range(len(self.list)):
            if "-" not in self.list[k]:
                pol+=" + "+self.list[k]
            elif "-" in self.list[k]:
                pol+=self.list[k]
        print(pol)
    
    def add(p1,p2):
        list2=[]
        for i in range(5):
            r=p1.cofficient_list[i]+p2.cofficient_list[i]
            list2.append(r)
        sum_of_polynomials=polynomial(list2[0],list2[1],list2[2],list2[3],list2[4],"x")
        sum_of_polynomials.create_cofficient_list()
        # sum_of_polynomials.print_cofficient_list()
        sum_of_polynomials.create_polynomial()
        sum_of_polynomials.print_polynomial()
        
    

def main():
    p1=polynomial(-1,1,-2,-3,-4,"x")
    p1.create_cofficient_list()
    # p1.print_cofficient_list()
    p1.create_polynomial()
    p1.print_polynomial()
    p2=polynomial(5,6,7,8,9,"x")
    p2.create_cofficient_list()
    # p2.print_cofficient_list()
    p2.create_polynomial()
    p2.print_polynomial()
    p1.add(p2)
main()