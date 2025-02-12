import math


"""n this script, define a base class Shape with a method area() and derived classes Rectangle and Circle, each overriding the area() method to calculate their respective areas."""


class Shape:
    """base class defined"""

"""Method: area(self), which simply raises a NotImplementedError, indicating that derived classes need to override this method."""
    def area(self):
        raise NotImplementedError("derived classes need to override this method")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
