#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for rows in range(len(matrix)):
            for columns in range(len(matrix)):
                if columns == len(matrix) - 1:
                    print("{}".format(matrix[rows][columns]))
                else:
                    print("{}".format(matrix[rows][columns]), end=" ")
    else:
        print("")
