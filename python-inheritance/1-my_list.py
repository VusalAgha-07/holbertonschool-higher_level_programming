#!/usr/bin/python3
"""Module that defines a class MyList that inherits from list."""


class MyList(list):
    """A subclass of list with additional sorting functionality."""

    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        print(sorted(self))
