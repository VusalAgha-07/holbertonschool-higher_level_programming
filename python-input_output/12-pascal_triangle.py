#!/usr/bin/python3
"""
This module contains a function that returns a Pascal's triangle.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    the Pascal's triangle of n.

    Args:
        n (int): The number of rows of the triangle.

    Returns:
        list: A list of lists representing the triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    while len(triangle) < n:
        prev_row = triangle[-1]
        # Every row starts with 1
        new_row = [1]

        # Calculate the numbers between the first and last elements
        for i in range(len(prev_row) - 1):
            new_row.append(prev_row[i] + prev_row[i + 1])

        # Every row ends with 1
        new_row.append(1)
        triangle.append(new_row)

    return triangle
