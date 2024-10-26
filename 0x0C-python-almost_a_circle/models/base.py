#!/usr/bin/python3
"""A class that manages the ID attriute across classes."""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries.
        Args:
            list_dictionaries (list): A list of dictionaries.
        Returns:
            str: JSON string representation of list_dictionaries, or "[]"
            if list_dictionaries is None or empty.
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)
