#!/usr/bin/python3
""" Base Model for the HBnB program.
    """

from datetime import datetime
from models import storage
import uuid


class BaseModel:
    """ Base Model for all classes used on HBnB.
        """

    def __init__(self, *args, **kwargs):
        """ Initializes the BaseModel as base-class for the program.
            """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            if "__class__" in kwargs.keys():
                del kwargs["__class__"]
            if "created_at" in kwargs.keys():
                c_new_value = datetime.fromisoformat(kwargs["created_at"])
                kwargs["created_at"] = c_new_value
            if "updated_at" in kwargs.keys():
                u_new_value = datetime.fromisoformat(kwargs["updated_at"])
                kwargs["updated_at"] = u_new_value
            self.__dict__.update(**kwargs)
        storage.new(self)

    def __str__(self):
        """ Prints an instances representation.
            """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """ Updates the instance updated_at attribute.
            """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ Returns a dict() with all keys/values of instance.__dict__
            """
        dictionary = dict()
        for (key, value) in (self.__dict__).items():
            if isinstance(value, datetime):
                dictionary[key] = value.isoformat()
            else:
                dictionary[key] = value
        dictionary["__class__"] = self.__class__.__name__
        return (dictionary)
