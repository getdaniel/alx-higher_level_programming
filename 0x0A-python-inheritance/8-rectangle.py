#!/usr/bin/python3
'''Define an empty class BaseGeometry'''


class BaseGeometry:
    '''Represent base geometry.'''

    def area(self):
        '''Not yet implemented.'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''Validate a parameters as an integer.

        Args:
           name (str): The name of the parameter.
           value (int): The parameter to validate.
        Raises:
           TypeError: If the value is not an integr.
           ValueError: If the value is <= 0.
        '''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


'''Defines a class Rectangle that inherits from BaseGeometry.'''


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
