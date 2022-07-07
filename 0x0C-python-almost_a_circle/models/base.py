#!/usr/bin/python3
'''Defines a Base model class.'''
import json


class Base():
    '''Represent a base model.

    Attribute:
       __nb_objects (): The number of instantiated bases.
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''Initialize a new base.

        Args:
           id (int): The identity of a new base.
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        '''Returns the JSON string representation of list_dictionaries.

        Args:
           list_dictionaries (list): A list of dictionaries.
        '''
        if list_dictionaries is None or list_dictionaries == []:
            return '[]'
        return json.dumps(list_dictionaries)
