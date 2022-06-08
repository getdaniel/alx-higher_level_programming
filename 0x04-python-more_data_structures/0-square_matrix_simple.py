#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    '''Computes the square value of all integers of matrix'''
    return ([list(map(lambda x: x * x, row)) for row in matrix])
