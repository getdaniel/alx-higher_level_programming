#!/usr/bin/python3
'''Defines a method that checks the object wether instance or not.'''


def is_same_class(obj, a_class):
    '''Checks whether an object is instance or not from a given class.

    Args:
        obj (any): The object to chech.
        a_class (type): The class to match the type of obj to.
    Return:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    '''
    if type(obj) == a_class:
        return True
    return False
