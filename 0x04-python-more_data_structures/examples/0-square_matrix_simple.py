#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    my_matrix = []
    i = 0
    j = 0
    while i < len(matrix):
        my_matrix.append([])
        j = 0
        while j < len(matrix[i]):
            my_matrix[i].append(matrix[i][j] ** 2)
            j += 1
        i += 1
    return my_matrix
