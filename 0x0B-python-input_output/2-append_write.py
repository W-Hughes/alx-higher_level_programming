#!/usr/bin/python3
"Function appends a string to the end of a UTF8 text file."""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a UTF8 file text file and
    return the number of characters added.

    args:
        filename (str): The name of the file to append to.
        text 9str): The text to append to the file.

    Returns:
        int: The number of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
