#!/usr/bin/python3
"""Defines an object attribute lookup function."""


def lookup(obj):
    """Returns a list of avalible attributes."""
    return (dir(obj))
