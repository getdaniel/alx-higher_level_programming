#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    '''Prints the first x elements of a list and only integer'''
    count = 0
    errors = 0

    while count < x:
        try:
            print("{:d}".format(my_list[count]), end="")
            count += 1
        except (ValueError, TypeError):
            count += 1
            errors += 1
    count -= errors
    print()

    return (count)
