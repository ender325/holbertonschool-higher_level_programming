#!/usr/bin/python3
"""
Defines a Square class.
"""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes a new Square.

        Args:
            size (int): The size of the square.
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
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates and returns the current square area.

        Returns:
            int: The area of the square (size squared).
        """
        return self.__size * self.__size

    def my_print(self):
        """Prints the square with the character '#' in stdout."""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            print("#" * self.__size)
