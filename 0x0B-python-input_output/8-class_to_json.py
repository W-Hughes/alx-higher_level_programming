#!/usr/bin/python3
"""Represents a class_to_json function that returns dictionary
description of object for JSON serialization"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    for JSON serialization of an object.
    Args:
        obj: An instance of a class.
    Returns:
        A dictionary representation of the object's attributes.
    """
    return obj.__dict__
