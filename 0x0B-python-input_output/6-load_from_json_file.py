#!/usr/bin/python3
"""Represents a load_from_jason_file function that
creates an Object fron a JSON file.
"""
import json


def load_from_json_file(filename):
    """Creates an Object from a JSON file.
    args:
        filename: file to create a JSON object from.
    """
    with open(filename, 'r') as file:
        return json.load(file)
