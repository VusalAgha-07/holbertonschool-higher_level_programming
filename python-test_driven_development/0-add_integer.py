#!/usr/bin/python3
"""
This is the "0-add_integer" module.
The module supplies one function, add_integer(), which adds two numbers.
Floats are casted to integers before the operation.
"""


def add_integer(a, b=98):
    """
    Adds 2 integers or floats.
    Args:
        a: first number (int or float)
        b: second number (int or float), defaults to 98
    Returns:
        The sum of a and b as an integer.
    Raises:
        TypeError: If either a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
