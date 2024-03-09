#!/usr/bin/python3
"""Defines the fundamental BaseModel class.
"""

import models
from datetime import datetime
from uuid import uuid4


tFormat = "%Y-%m-%dT%H:%M:%S.%f"
# cl_Name = ""
#new_Dict = ""


class BaseModel:
    """The BaseModel serves as the foundation from which future classes will inherit."""

    def __init__(self, *args, **kwargs):
        """Initialization of BaseModel class

        Args:
            *args: Unused.
            **kwargs (dict): key/value pairs of attr
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, tFormat)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)


    def save(self):
        """Updates or timestamps the attribute "update_at" with the current datetime."""
        self.update_at = datetime.now()
        model.storage.save()

    def __str__(self):
        """Return the string representation of the BaseModel instance for printing."""
        cl_Name = self.__class__.__name__
        return "[{}] ({}) {}".format(cl_Name, self.id, self.__dict__)

    def to_dict(self):
        """Return a dictionary representing the BaseModel instance.

        Including the key/value pair "__class__"
        indicating the object's class name.
        """
        new_Dict = self.__dict__.copy()
        new_Dict["created_at"] = self.created_at.isoformat()
        new_Dict["updated_at"] = self.updated_at.isoformat()
        new_Dict["__class__"] = self.__class__.__name__
        return new_Dict



