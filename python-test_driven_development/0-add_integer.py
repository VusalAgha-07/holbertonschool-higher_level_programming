#!/usr/bin/python3
"""
This module provides a function for integer addition.
The function add_integer adds two numbers (ints or floats).
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats together.

    Args:
        a: The first number, must be an int or float.
        b: The second number, must be an int or float (defaults to 98).

    Returns:
        The sum of a and b as an integer.

    Raises:
        TypeError: If a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
