#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represents a Rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): the height of the new Rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the Rectagle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the Rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the Rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Computes and returns the area of the Rectangle."""
        return (self.width * self.height)

    def perimeter(self):
        """Computes and returns the perimeter of the Rectangle.
        If either width or perimeter is 0, perimeter is 0.
        """
        if (self.width == 0 or self.height == 0):
            return 0
        return (2 * (self.width + self.height))

    def __str__(self):
        """Returns a string representation of the Rectangle using '#'.
        If width or height is 0, return an empty string.
        """
        if self.width == 0 or self.height == 0:
            return ("")
        return '\n'.join(['#' * self.width for _ in range(self.height)])

    def __repr__(self):
        """Return a string representation of the Rectangle that can be
        recreated with a new instance using eval().
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Print a message when an instace of Rectangle is deleted."""
        print("Bye rectangle...")
