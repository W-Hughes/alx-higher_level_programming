#!/usr/bin/python3
"""Represents an Object-writing function using JSON representation."""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation."""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
