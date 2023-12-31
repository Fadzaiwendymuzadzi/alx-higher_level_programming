#!/usr/bin/python3
""" In this module base class is defined """
import json


class Base:
    """ Base class is the base class for all other classes in the project

    Arg():
        id (int): the identification of the objetc.

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes the values of the function considering edge cases."""
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

        elif id is not None:
            if id > 0:
                self.id = id
            else:
                msg = "id must be a positive integer greater than 0"
                raise ValueError(msg)

    @classmethod
    def reset_nb(self):
        """ Resets the number of instances created. """
        self.__nb_objects = 0

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns json string representation of a list of dictionaries.

        Args:
            list_dictionaries (list): list with dictionaries that representobj.

        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): list of objects to copy to a file.

        """
        filename = "{}.json".format(cls.__name__)
        list_dict = []
        if list_objs:
            for i in list_objs:
                list_dict.append(i.to_dictionary())
        message_write = cls.to_json_string(list_dict)
        with open(filename, "w", encoding='utf-8') as file:
            file.write(message_write)

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation json_string. """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Creates a new instance of a class.

        Args:
            dictionary (**): dictionary with values of attributes.

        """
        if cls.__name__ == "Rectangle":
            if len(dictionary) < 2:
                raise TypeError("Not enough arguments")
            new = cls(1, 2)
        else:
            if len(dictionary) < 1:
                raise TypeError("Not enough arguments")
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances. """
        filename = str(cls.__name__) + ".json"
        list_instances = []
        try:
            with open(filename, "r") as file:
                line = file.readline()
        except:
            return []

        for dictionary in cls.from_json_string(line):
            new = cls.create(**dictionary)
            list_instances.append(new)
        return list_instances
