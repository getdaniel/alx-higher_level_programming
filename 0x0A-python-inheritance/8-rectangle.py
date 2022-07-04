#!/usr/bin/python3
'''Defines a class Rectangle that inherits from BaseGeometry.'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Represent a rectangle that inherits from BaseGeometry.'''

    def __init__(self, width, height):
        '''Initialize a new Rectangle.

        Args:
           width (int): The width of the new Rectangle.
           height (int): The height of the new Rectangle.
        '''
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
