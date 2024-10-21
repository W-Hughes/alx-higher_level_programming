#!/usr/bin/python3
"""A class that manages the ID attriute across classes."""


class Base:
    """Base class for managing 'id' attribute across future classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialze a Base Instance
        Args:
            id (int): the id of the instance. if None, it
            will automatically assigned.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
