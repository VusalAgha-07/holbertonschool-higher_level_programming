#!/usr/bin/python3
"""Module that defines a function to check if an object is exactly
an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a specified class.

    Args:
        obj: The object to check.
        a_class: The class to match against.

    Returns:
        True if obj is exactly an instance of a_class, otherwise False.
    """
    return type(obj) is a_class
