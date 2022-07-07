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

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Returns the JSON string representation of list_dictionaries.

        Args:
           list_dictionaries (list): A list of dictionaries.
        '''
        if list_dictionaries is None or list_dictionaries == []:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''Writes the JSON string representation of list_objs to a file.

        Args:
           cls (obj): Classes.
           list_objs (list): A list of instances who inherits of Base.
        '''
        filename = cls.__name__ + ".json"
        with open(filename, "w") as myfile:
            if list_objs is None:
                myfile.write("[]")
            else:
                list_dict = [op.to_dictionary() for op in list_objs]
                myfile.write(Base.to_json_string(list_dict))

    def from_json_string(json_string):
        '''Returns the list of the JSON string representation json_string.

        Args:
           json_string (str): A string representing a list f dictionaries.
        '''
        if json_string is None or json_string == []:
            return '[]'
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''Returns an instance with all attributes already set.

        Args:
           cls (obj): Classes.
           **dictionary (dict): A double pointer to a dictionary.
        '''
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)

            return new

    @classmethod
    def load_from_file(cls):
        '''Returns a list of instances.'''
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, 'r') as myfile:
                list_dict = Base.from_json_string(myfile.read())
                return [cls.create(**dic) for dic in list_dict]
        except IOError:
            return []
