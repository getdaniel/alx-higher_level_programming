#!/usr/bin/python3
def best_score(a_dictionary):
    '''R`eturns a key with the biggest integer value.'''
    if not a_dictionary:
        return None
    return max(a_dictionary)