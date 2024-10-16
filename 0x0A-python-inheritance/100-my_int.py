#!/usr/bin/python3
"""Defines a rebel MyInt class that inherits from int."""


class MyInt(int):
    """MyInt class with inverted == and != operators."""

    def __eq__(self, other):
        """Inverts the behavior of the equality operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Inverts the behavior of the not equal operator."""
        return super().__eq__(other)
