#!/usr/bin/python3
def magic_calculation(a, b):
    '''pythoncode style'''
    result = 0
    for index in range(1, 3):
        try:
            if index > a:
                raise Exception('Too far')
            else:
                result += a ** b / index
        except:
            result = b + a
            break
        return (result)

