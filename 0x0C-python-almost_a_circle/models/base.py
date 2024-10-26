#!/usr/bin/python3
"""A class that manages the ID attriute across classes."""
import json
import os
import csv


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

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file.
        Args:
            list_objs ((list): A list of instances inherited from Base.
        """
        filename = f"{cls.__name__}.json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of dictionaries represented by json_string.

        Args:
            json_string (str): A JSON string representing a
            list of dictionaries.

        Returns:
            list: A list of dictionaries represented by json_string,
            or an empty list if json_string is None or empty.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates an instance with attributes set according to dictionary.
        Args:
            **dictionary: Key-value pairs of attributes to initialize instance.
        Returns:
            An instance of cls with attributes set.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Loads a list of instances from a file.
        Returns:
            List: A list of instances of cls, or an empty list
            if the file does not exit.
        """
        filename = f"{cls.__name__}.json"
        if not os.path.exists(filename):
            return []
        with open(filename, "r") as file:
            json_string = file.read()
            list_dicts = cls.from_json_string(json_string)
            return [cls.create(**d) for d in list_dicts]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves a list of objects to a CSV file."""
        filename = f"{cls.__name__}.csv"
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            if list_objs is None or len(list_objs) == 0:
                return
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([obj.id, obj
                                    .width, obj.height, obj.x, obj.y]
                                    )
                elif cls.__name__ == "Square":
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Loads a list of instances from a CSV file."""
        filename = f"{cls.__name__}.csv"
        if not os.path.exists(filename):
            return []
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            list_instances = []
            for row in reader:
                if cls.__name__ == "Rectangle":
                    rect = cls(
                        int(row[1]),
                        int(row[2]),
                        int(row[3]),
                        int(row[4]),
                        int(row[0])
                    )
                elif cls.__name__ == "Square":
                    rect = cls(
                        int(row[1]),
                        int(row[2]),
                        int(row[3]),
                        int(row[0])
                    )
                list_instances.append(rect)
            return list_instances
