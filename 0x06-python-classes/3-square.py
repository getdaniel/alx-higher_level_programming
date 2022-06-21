#!/usr/bin/python3
'''Defines a sqaure by'''


class Square:
    '''Define a class Square'''
    def __init__(self, size=0):
        '''Initialize a new square.

        Args:
           size (int): The size of the new square.
        '''
        if not isinstance(size, int):
            raise TypeError()
        elif size < 0:
            raise ValueError()
        self.__size = size

    def area(self):
        '''Return the area of the square.'''
        return (self.__size * self.__size)
