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

    def integer_validator(self, name, value):
        """
        Validates if the value is a positive integer.

        Args:
            name (str): The parameter name (assumed to be a string).
            value (int): The value to validate.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
