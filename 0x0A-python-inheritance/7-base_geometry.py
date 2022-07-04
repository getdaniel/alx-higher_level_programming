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
