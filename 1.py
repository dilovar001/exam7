# class Davra:
#     PI= 3.14
#     def __init__(self,radius):
#         self.radius=radius
#     def radiuss(self):
#         return 2*self.PI*self.radius*self.radius
# davra=Davra(2)


# class krug:
#   PI = 3.14

#   def __init__(self, radius):
#     self.radius = radius

#   def ploshad(self):
#     return krug.PI * self.radius * 2

#   def perimetr(self):
#     return 2 * krug.PI * self.radius

#   def __str__(self):
#     return self.radius

# krug1 = krug(2)

# print(krug) 
# print(f"Площадь круга1: {krug1.perimetr()}")  
# print(f"Периметр круга1: {krug1.perimetr()}")  




class Circle:
    PI=3.14
    def __init__(self,radius:int):
        self.radius=radius
    def get_area(self):
        return 2*self.PI * self.radius * self.radius
    def get_diametr(self):
        return 2 * self.radius
    def get_circumference(self):
        return 2 * self.PI * self.radius
    def get_radius(self):
        return self.radius
name=Circle(2)
print(name.get_area())
print(name.get_diametr())
print(name.get_circumference())
print(name.get_radius())