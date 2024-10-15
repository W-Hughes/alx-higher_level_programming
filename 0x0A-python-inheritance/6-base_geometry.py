#!/usr/bin/python3
"""Defines a base class BaseGeometry."""


class BaseGeometry:
    """A base class for geometry-related operations."""

    def area(self):
        """
        Public instance method that raises an exception.
        Raises:
            Exception: with the message "area() is not implemented."
        """
        raise Exception("area() is not implemented")
