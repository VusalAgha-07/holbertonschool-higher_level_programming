#!/usr/bin/python3
"""Module that defines a function to check if an object is an instance
of a class that inherited from a specified class.
"""


def inherits_from(obj, a_class):
    """Check if an object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to match against.

    Returns:
        True if obj inherited from a_class and is not an instance
        of a_class itself, otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
