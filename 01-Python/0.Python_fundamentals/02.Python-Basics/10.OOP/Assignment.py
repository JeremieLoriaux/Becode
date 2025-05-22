"""
## Understand the basics of Inheritance and Overriding
Design a base class Shape with a method area() that calculates the area
(set to 0 by default).
Create subclasses Square and Circle that inherit from Shape and override the
area() method with
their specific area calculations based on side length and radius, respectively.
"""
from math import pi


class Shape:
    """
    Base class for shapes.
    """

    def area(self):
        """
        Method to calculate the area of a shape.
        The default value is 0
        """
        return 0


class Square(Shape):
    """
    Subclass of the Shape class that designates a square.
    """

    def __init__(self, side: float):
        self.side = side

    def area(self):
        """
        overrides the inherited area method from the Shape class to calculate
        the area of a square.
        """
        return self.side ** 2


class Circle(Shape):
    """
    Subclass of the Shape class that designates a circle
    """
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        """
        overrides the inherited area method from the Shape class to calculate
        the area of a circle
        """
        return pi * self.radius ** 2


# create test shapes
test_shape = Shape()
test_square = Square(4)
test_circle = Circle(9)

# testing code
print(test_shape.area())
print(test_circle.area())
print(test_square.area())
