#!/usr/bin/python3
"""Defines a Square class that inherits from the Rectangle class."""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a Square class,
    which is a specialized case of a rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Intialize a new Square.
        Args:
            size (int): The size of the square (both width and height)
            x (int): The x position.
            y (int): the yp position.
            id (int): the identity of the square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return the string representation of the square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """Getter for size (Note: width == height)"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size, setting both width and height."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square.
        Args:
            args (ints): New attribute values.
            - 1st argument represents id attribute.
            - 2nd argument represents size attribute
            - 3rd argument represents x attribute
            - 4th argument represents y atttribute
        kwargs (dict): New keyworded arguments
        """
        attributes = ['id', 'size', 'x', 'y']
        if args and len(args) > 0:
            for i, value in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], value)
        elif kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of a Square."""
        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
            }
