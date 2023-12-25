#FUNCTION OVERRIDING 
#WHEN PARENT AND CHILD BOTH HAVE SAME FUNCTIONS,PROTOTYPE,previously discussed
import math

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Rectangle):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


# Creating instances of shapes
rectangle = Rectangle(4, 6)
circle = Circle(5)

# Calculating area for each shape
print(f"Rectangle - Area: {rectangle.area()}")
print(f"Circle - Area: {circle.area()}")
