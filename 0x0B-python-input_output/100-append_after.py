#!/usr/bin/python3
"""
Inserts a line of text to a file after
eachline containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts `new_string` after each line in `filename`
    that contains `search_string`.
    Args:
        filename (str): The name of the file to be modified.
        search_string (str): The string to search for in the file.
        new_string (str): The string to insert after
        lines containing `search_string`.
    """
    with open(filename, "r") as file:
        lines = file.readlines()

    with open(filename, "w") as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)