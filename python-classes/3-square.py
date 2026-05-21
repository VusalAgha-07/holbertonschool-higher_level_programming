#!/usr/bin/python3
"""Module that defines a Square class with area calculation."""


class Square:
    """This class represents a square."""

    def __init__(self, size=0):
        """Initializes the square with size validation.

        Args:
            size (int): The size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Method that returns the current area of the square."""
        return self.__size * self.__size
