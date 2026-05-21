#!/usr/bin/python3
"""Module that defines a Square class with a print method."""


class Square:
    """This class represents a square."""

    def __init__(self, size=0):
        """This sets the square size.

        Args:
            size (int): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """This gets the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """This sets the size with checks."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """This returns the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """This prints the square with the # character."""
        # Əgər ölçü 0-dırsa, sadəcə boş bir sətir çap edirik.
        if self.__size == 0:
            print("")
            return

        for i in range(self.__size):
            print("#" * self.__size)
