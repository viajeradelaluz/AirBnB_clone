#!/usr/bin/python3
"""
Base Model for HBnB
"""

from abc import ABC, abstractmethod
from datetime import datetime
from models.__init__ import storage
import uuid

class BaseModel(ABC):
    """
    Base Model for all classes used on HBnB
    """

    def __init__(self, *args, **kwargs):
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            if "__class__" in kwargs.keys():
                del kwargs["__class__"]
            if "created_at" in kwargs.keys():
                kwargs["created_at"] = datetime.fromisoformat(kwargs["created_at"])
            if "updated_at" in kwargs.keys():
                kwargs["updated_at"] = datetime.fromisoformat(kwargs["updated_at"])
            self.__dict__.update(**kwargs)

    def __str__(self):
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        ret_dict = dict()
        for (key, value) in (self.__dict__).items():
            if isinstance(value, datetime):
                ret_dict[key] = value.isoformat()
            else:
                ret_dict[key] = value
        ret_dict["__class__"] = self.__class__.__name__
        return (ret_dict)
