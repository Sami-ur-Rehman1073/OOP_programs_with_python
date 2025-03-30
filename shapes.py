# Write a program for shapes.

class canvas:

    def __init__(self,border_colour,backgroud_colour):
        self.border_colour=border_colour
        self.backgroud_colour=backgroud_colour

class shapes:

    def __init__(self,name,border_color,back_color,x_point,y_point):
        self.shape_name=name
        self.border_colour=border_color
        self.background_colour=back_color
        self.x_dimension=x_point
        self.y_dimension=y_point
    
    def __str__(self):
        s=f"{self.shape_name}, {self.border_colour}, {self.background_colour}, {self.x_dimension}, {self.y_dimension}"
        return s

class square(shapes):

    def __init__(self,name,border_color,back_color,x_point,y_point,length_of_side):
        super().__init__(name,border_color,back_color,x_point,y_point)
        self.length=length_of_side

    def calculate_perimeter(self):
        self.perimeter=4*self.length

    def calculate_area(self):
        self.area=self.length*self.length

    def __str__(self):
        s=super().__str__()
        return f"{s}, {self.length}, {self.perimeter}, {self.area}"
    
class rectangle(shapes):

    def __init__(self,name,border_color,back_color,x_point,y_point,length_of_side,width_of_side):
        super().__init__(name,border_color,back_color,x_point,y_point)
        self.length=length_of_side
        self.width=width_of_side

    def calculate_perimeter(self):
        self.perimeter=2*(self.length+self.width)

    def calculate_area(self):
        self.area=self.length*self.width

    def __str__(self):
        s=super().__str__()
        return f"{s}, {self.length}, {self.perimeter}, {self.area}"
    
class circle(shapes):

    pi=3.1416

    def __init__(self,name,border_color,back_color,x_point,y_point,radius_of_circle):
        super().__init__(name,border_color,back_color,x_point,y_point)
        self.radius=radius_of_circle

    def calculate_circumference(self):
        self.circumference=2*self.pi*self.radius

    def calculate_area(self):
        self.area=self.pi*self.radius*self.radius

    def __str__(self):
        s=super().__str__()
        return f"{s}, {self.radius}, {self.circumference}, {self.area}"
    

class triangle(shapes):

    pi=3.1416

    def __init__(self,name,border_color,back_color,x_point,y_point,l1,l2,l3):
        super().__init__(name,border_color,back_color,x_point,y_point)
        self.length1=l1
        self.length2=l2
        self.length3=l3

    def calculate_perimeter(self):
        self.perimeter=self.length1+self.length2+self.length3

    def calculate_area(self):
        self.area=0.5*(self.length1*self.length2)

    def __str__(self):
        s=super().__str__()
        return f"{s}, {self.length1}, {self.length2}, {self.length3}, {self.perimeter}, {self.area}"
    


def main():
    s1=triangle("triangle","blue","Yellow",26,27,4,5,6)
    s2=circle("circle","blue","Yellow",26,27,4)
    s1.calculate_area()
    s1.calculate_perimeter()
    s2.calculate_area()
    s2.calculate_circumference()
    print(s1)
    print(s2)

main()