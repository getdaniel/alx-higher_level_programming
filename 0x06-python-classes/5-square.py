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
        '''Get/set the current size of the square.'''
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''Return the area of square.'''
        return (self.__size * self.__size)

    def my_print(self):
        '''Print the square with the number character.'''
        for index in range(0, self.__size):
            [print("#", end="") for jndex in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
