#!/usr/bin/python3
def safe_function(fct, *args):
    '''Executes a function safely'''
    import sys
    try:
        run = fct(*args)
        return (run)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
