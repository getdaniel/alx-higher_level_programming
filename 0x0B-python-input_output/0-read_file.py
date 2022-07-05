#!/usr/bin/python3
'''Define a text file-reading function.'''


def read_file(filename=""):
    '''Print the content of a UTF-8 text file to stdout.'''
    with open(filename, encoding="utf-8") as myfile:
        print(myfile.read(), end="")
