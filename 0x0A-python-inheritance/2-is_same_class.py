#!/usr/bin/python3
"""Checks class instantiations of objects."""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.

    Returns:
        True if obj is exactly an instance of a_class; otherwise, False.
    """
    return isinstance(obj, a_class) and type(obj) is a_class