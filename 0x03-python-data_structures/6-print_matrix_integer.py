#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for rows in range(len(matrix)):
        for columns in range(len(matrix)):
            if columns == len(matrix) - 1:
                print("{:d}".format(matrix[rows][columns]))
            else:
                print("{:d}".format(matrix[rows][columns]), end=" ")
