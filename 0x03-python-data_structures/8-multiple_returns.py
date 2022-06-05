#!/usr/bin/python3
def multiple_returns(sentence):
    '''Returns a tuple with the length of a string and its first character.'''
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
