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
        '''
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)
