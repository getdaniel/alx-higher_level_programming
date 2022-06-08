#!/usr/bin/python3
def weight_average(my_list=[]):
    '''Returns the weighted average of all integers tuple'''
    if not isinstance(my_list, list) or len(my_list) == 0:
        return (0)

    avg = 0
    size = 0
    for tupple in my_list:
        avg += (tupple[0] * tupple[1])
        size += tupple[1]
    return (avg / size)
