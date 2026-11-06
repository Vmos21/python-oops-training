from math import pi
class Shape:
    def __init__(self, name):
        self.name = name
    def area():
        pass

class Circle(Shape):
    def __init__(self, r):
        super().__init__("Circle")
        self.radius = r

    def area(self):
        return pi*self.radius**2

class Rectangle(Shape):
    def __init__(self, l, b):
        super().__init__("Rectangle")
        self.length = l
        self.breadth = b

    def area(self):
        return self.length*self.breadth

c = Circle(5)
r = Rectangle(4, 6)
print(c.name, ":", c.area())
print(r.name, ":", r.area())