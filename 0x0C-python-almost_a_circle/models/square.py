#!/usr/bin/python3
'''Define the class Square.'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Represent Square class.'''

    def __init__(self, size, x=0, y=0, id=None):
        '''Initialize the new Square object.

        Args:
           size (int): The size of the square.
           x (int): The x coordinate of the square.
           y (int): The y coordinate of the square.
           id (int): The identity of the square.
        '''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''Return [Square] (<id>) <x>/<y> - <size> format.'''
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y,
                                                 self.height)

    @property
    def size(self):
        '''Get/Set the size of the square.'''
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''Update the square attributes.

        Args:
           *args (ints): The list of arguments - no-keyworded arguments.
               - 1st argument should be the id attribute.
               - 2nd argument should be the size attribute.
               - 3rd argument should be the x attribute.
               - 4th argument should be the y attribute.
            **kwargs (dict): A double pointer to a dictionary: key/value.
        '''
        if args and len(args) != 0:
            argument = 0
            for arg in args:
                if argument == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif argument == 1:
                    self.size = arg
                elif argument == 2:
                    self.x = arg
                elif argument == 3:
                    self.y = arg
                argument += 1
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'id':
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == 'size':
                    self.size = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def to_dictionary(self):
        '''Returns the dictionary representation of a Square.'''
        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }
