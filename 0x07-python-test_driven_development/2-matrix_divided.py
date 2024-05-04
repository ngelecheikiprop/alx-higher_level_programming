#!/usr/bin/python3
"""contains the following functions:
    -matrix_divided - to divide elements of a matrix by a number given
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix
    Args:
        matrix -  a list of integers or floats
        div - value to divide all the numbers in the matrix
    Returns:
        Returns a new matrix with all values divided by div
    """
    for i in matrix:
        if type(i) is not list:
            raise TypeError("matrix must be a matrix (list of lists)",
                            " of integers/floats")
        for j in i:
            if type(j) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists)",
                                " of integers/floats")

    for x in range(len(matrix) - 1):
        if len(matrix[x]) != len(matrix[x + 1]):
            raise TypeError("Each row of the matrix must have the same size")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    new_matrix = []
    index = 0
    for i in matrix:
        new_matrix.append([])
        for j in i:
            new_matrix[index].append(round((j / div), 2))
        index += 1
    return new_matrix
