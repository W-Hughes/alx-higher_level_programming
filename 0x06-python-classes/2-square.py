#!/usr/bin/python3

"""Define a Square Class"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initialize the square class with a private size attribute.
        Args:
            size (int): The size of the square *default is 0).

        Raises:
            TypeError: if `size` is not an integer.
            ValueError: if `size` is less than 0.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
