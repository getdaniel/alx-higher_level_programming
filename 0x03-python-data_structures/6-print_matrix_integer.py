#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    '''Print a matrix of integers'''
    for index in range(len(matrix)):
        for jndex in range(len(matrix[index])):
            print("{:d}".format(matrix[index][jndex]), end="")
            if jndex != (len(matrix[index]) - 1):
                print(" ", end="")

        print("")
