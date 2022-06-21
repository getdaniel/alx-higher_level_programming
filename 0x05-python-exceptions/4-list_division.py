#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    '''Divides elements by element 2 lists.'''
    new_list = []
    count = 0

    while count < list_length:
        try:
            div = my_list_1[count] / my_list_2[count]
        except TypeError:
            div = 0
            print("Wrong type")
        except ZeroDivisionError:
            div = 0
            print("division by 0")
            div = 0
        except IndexError:
            div = 0
            print("out of range")
        finally:
            count += 1
            new_list.append(div)
    return (new_list)
