#!/usr/bin/python3
'''Define a Square class.'''


class Square:
    '''Define a class Square'''
    def __init__(self, size=0):
        '''Initialize a new square.
        Args:
           size (int): The size of the new square.
        '''
        self.size = size

    @property
    def size(self):
        ''' Get the size of the Square.'''
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''Return the area of the Square.'''
        return (self.__size * self.__size)

    def __eq__(self, other):
        '''Defines == comparision.'''
        return self.area() == other.area()

    def __ne__(self, other):
        ''' Define != comparision.'''
        return self.area() != other.area()

    def __lt__(self, other):
        ''' Define < comparision.'''
        return self.area() < other.area()

    def __le__(self, other):
        ''' Define <= comparision.'''
        return self.area() <= other.area()

    def __gt__(self, other):
        ''' Define > comparision.'''
        return self.area() > other.area()

    def __ge__(self, other):
        ''' Define >= comparision.'''
        return self.area() >= other.area()
