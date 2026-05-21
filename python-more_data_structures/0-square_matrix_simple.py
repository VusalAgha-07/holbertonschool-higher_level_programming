#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Həm xarici, həm daxili dövrü bir sətirdə birləşdiririk
    return [[x ** 2 for x in row] for row in matrix]
