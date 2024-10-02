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
        self.__size = size

    @property
    def size(self):
        """Retrieves/Gets the size of the squre"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area."""
        return (self.__size ** 2)

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
