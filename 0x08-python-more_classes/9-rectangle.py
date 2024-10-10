#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represents a Rectangle."""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): the height of the new Rectangle
        """
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the Rectangle."""
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
        If either width or height is 0, perimeter is 0.
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
        return '\n'.join(
                [str(self.print_symbol) * self.width
                    for _ in range(self.height)]
        )

    def __repr__(self):
        """Return a string representation of the Rectangle that can be
        recreated with a new instance using eval().
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Print a message when an instance of Rectangle is deleted."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the Rectangle with the bigger area.
        if both have the same area, return rect_1.
        Args:
            rect_1 (Rectangle): The first rectangle.
            rect_2 (Rectangle): The second rectangle.
        Raises:
            TypeError: If rect_1 or rect_2 is not an instance of Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle instance with width == height == size.

        Args:
            size (int): The size of the new square.
        """
        return cls(size, size)
