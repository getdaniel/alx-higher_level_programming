#!/usr/bin/python3
'''Define an inherited class-checking function.'''


def inherits_from(obj, a_class):
    '''Checks an object is inherited instance of a class.

    Args:
       obj (any): The object to check.
       a_class (type): The class to match the type of obj to.
    Returns:
       If obj is inherited instance of a_class - True
       Otherwise - False.
    '''
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
