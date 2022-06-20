#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    '''Prints x elements of a list '''
    try:
        count = 0
        while count < x:
            print("{}".format(my_list[count]), end='')
            count += 1
        print()
        return count
    except IndexError:
        print()
        return count
    pass
