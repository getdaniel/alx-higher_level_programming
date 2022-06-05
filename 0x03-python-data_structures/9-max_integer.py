#!/usr/bin/python3
def max_integer(my_list=[]):
    '''Finds the biggest integer of a list.'''
    if len(my_list) == 0:
        return (None)

    big = my_list[0]
    for index in range(len(my_list)):
        if my_list[index] > big:
            big = my_list[index]

    return (big)
