#!/usr/bin/python3
'''Define a search and update function.'''


def append_after(filename="", search_string="", new_string=""):
    '''Inserts a line text to a file.

    Args:
       filename (str): The name of the file.
       search_string (str); The string to search for within the file.
       new_string (str): The string to insert.
    '''
    text = ""
    with open(filename) as myfile_r:
        for line in myfile_r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as myfile_w:
        myfile_w.write(text)
