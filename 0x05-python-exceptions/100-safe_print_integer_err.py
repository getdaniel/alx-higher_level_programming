#!/usr/bin/python3
def safe_print_integer_err(value):
    '''Prints an integer'''
    import sys
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError) as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return (False)
    else:
        return (True)
