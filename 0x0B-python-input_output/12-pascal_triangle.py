#!/usr/bin/python3
'''Defines pascal triangle function.'''


def pascal_triangle(n):
    '''Returns a list of lists of integers representing
       the Pascal’s triangle of n.

    Args:
       n (int): The size of triangle.
    Returns:
       A list of integer representingg the triangle.
    '''
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for index in range(len(tri) - 1):
            tmp.append(tri[index] + tri[index + 1])
        tmp.append(1)
        triangles.append(tmp)

    return triangles
