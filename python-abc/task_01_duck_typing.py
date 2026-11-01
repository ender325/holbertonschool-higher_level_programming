#!/usr/bin/python3
"""Defines an abstract base class Shape, concrete subclasses Circle and Rectangle,
and a duck-typing utility function shape_info.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class representing a geometric shape."""

    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape."""
        pass


class Circle(Shape):
    """Represents a Circle subclass inheriting from Shape."""

    def __init__(self, radius):
        """Initialize a new Circle.

        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """Return the area of the circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Return the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Represents a Rectangle subclass inheriting from Shape."""

    def __init__(self, width, height):
        """Initialize a new Rectangle.

        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Prints the area and perimeter of any object with area() and perimeter() methods.

    Relies entirely on duck typing without explicit type-checking.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")


if __name__ == "__main__":
    # Instantiate a Circle and a Rectangle
    my_circle = Circle(5)
    my_rectangle = Rectangle(4, 6)

    # Test the shape_info function
    print("--- Circle Information ---")
    shape_info(my_circle)

    print("\n--- Rectangle Information ---")
    shape_info(my_rectangle)
