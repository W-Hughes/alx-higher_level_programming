#!/usr/bin/python3
"""Defines a text writing-function."""


def write_file(filename="", text=""):
    """
    Writes strings to a UTF8 text file, and return
    the number of characters written.

    Args:
        filename (str): The name of the file to be written to.
        text (str): The text to write to the file.

    Returns:
        int: The number of characters written.
    """

    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
