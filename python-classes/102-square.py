#!/usr/bin/python3
"""
Defines a Square class.
"""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes a new Square.

        Args:
            size (int or float): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square with validation.

        Args:
            value (int or float): The new size of the square.

        Raises:
            TypeError: If value is not a number (integer or float).
            ValueError: If value is less than 0.
        """
        if type(value) not in (int, float):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates and returns the current square area.

        Returns:
            int or float: The area of the square (size squared).
        """
        return self.__size * self.__size

    def __eq__(self, other):
        """Defines the == comparison based on square area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Defines the != comparison based on square area."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Defines the < comparison based on square area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Defines the <= comparison based on square area."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Defines the > comparison based on square area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Defines the >= comparison based on square area."""
        return self.area() >= other.area()
