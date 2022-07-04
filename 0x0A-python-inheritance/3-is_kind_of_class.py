#!/usr/bin/python3
'''Defines a class and inherited classss-chking function.'''


def is_kind_of_class(obj, a_class):
    '''Check an object is instance or inherited instance of a class.

    Args:
       obj (any): The object to be checked.
       a_class (type): The class to match the type of obj to.
    Returns:
       If obj is an instance or inherited instance of a_class - True.
       Otherwise - False.
    '''
    if isinstance(obj, a_class):
        return True
    return False
