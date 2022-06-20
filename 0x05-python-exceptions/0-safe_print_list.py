#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    '''Prints x elements of a list '''
    result = 0

    for index in range(x):
        try:
            print("{}".format(my_list[index], end=""))
            result += 1
        except IndexError:
            break

    return (result)
