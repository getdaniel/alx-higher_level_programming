#!/usr/bin/python3
def safe_function(fct, *args):
    '''Executes a function safely'''
    import sys
    try:
        run = fct(*args)
        return (run)
    except Exception as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return (None)
