#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    '''Returns a new dictionary with all values multiplied by 2.'''
    return ({v: a_dictionary[v] * 2 for v in a_dictionary})
