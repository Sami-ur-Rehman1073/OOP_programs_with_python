# 3D vector class implementation

class vectors:
    def __init__(self,x,y,z):
        self.x_comp = x
        self.y_comp = y
        self.z_comp = z


    def __str__(self):
        self.signed_x_component = str(self.x_comp)
        if self.y_comp > 0:
            self.signed_y_comp = "+" + str(self.y_comp)
        else:
            self.signed_y_comp = str(self.y_comp)
        if self.z_comp > 0:
            self.signed_z_comp = "+" + str(self.z_comp)
        else:
            self.signed_z_comp = str(self.z_comp)
        return f"{self.x_comp}i{self.signed_y_comp}j{self.signed_z_comp}k"


    def __add__(self, v2):
        resultant_x = self.x_comp + v2.x_comp
        resultant_y = self.y_comp + v2.y_comp
        resultant_z = self.z_comp + v2.z_comp
        resultant = vectors(resultant_x, resultant_y, resultant_z)
        return resultant

    def substract_vectors(v1,v2):
        resultant_x = v1.x_comp - v2.x_comp
        resultant_y = v1.y_comp - v2.y_comp
        resultant_z = v1.z_comp - v2.z_comp
        resultant = vectors(resultant_x, resultant_y, resultant_z)
        print(resultant)

    def scalar_multiplication(self, c):
        resultant_x = self.x_comp * c
        resultant_y = self.y_comp * c
        resultant_z = self.z_comp * c
        resultant = vectors(resultant_x, resultant_y, resultant_z)
        print(resultant)

    def is_unit_vector(self):
        if self.x_comp + self.y_comp + self.z_comp == 0:
            print("Gvien vector is a unit vector")
        else:
            print("Gvien vector is not a unit vector")

def main():
    v1 = vectors(-2,3,-4)
    print(v1)
    v2 = vectors(0,2,7)
    print(v2)
    print(v1+v2) 
    v1.substract_vectors(v2)
    # v1.is_unit_vector()
main()