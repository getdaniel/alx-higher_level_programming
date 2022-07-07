#!/usr/bin/python3
'''Defines class Rectangle.'''
from models.base import Base


class Rectangle(Base):
    '''Represent a Rectangle class.'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Initialize a new Rectangle.

        Args:
           width (int): The width of the rectangle.
           height (int): The height of the rectangle.
           x (int): The x coordinate of the rectangle.
           y (int): The y coordinate of the rectangle.
           id (int): The identity of the rectangle.
        Raises:
           TypeError: If the input is not an integer.
           ValueError: If width/height is <= 0.
        '''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''Set/Get the width of rectangle.'''
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''Set/Get the height of rectangle.'''
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''Set/Get the x coordinates of rectangle.'''
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''Set/Get the y coordinates of rectangle.'''
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''Calculates the area of the rectangle.'''
        return self.width * self.height
