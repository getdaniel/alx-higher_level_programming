#!/usr/bin/python3
'''Define append a string to  a text file function.'''


def append_write(filename="", text=""):
    '''Append a text file to  a filename.

    Args:
       filename (str): The file that a text file append.
       text (str): The text to be append.
    Returns:
       The number of character that appended.
    '''
    with open(filename, "a", encoding="utf-8") as myfile:
        return (myfile.write(text))
