#!/usr/bin/python3
"""Defines the fundamental BaseModel class.
"""

import models
from datetime import datetime
from uuid import uuid4


tFormat = "%Y-%m-%dT%H:%M:%S.%f"
coreName = ""
newDict = ""


class BaseModel:
    """The BaseModel serves as the foundation from which future classes will inherit."""

    def __init__(self, *args, **kwargs):
        """Initialization of BaseModel class"""


    def save(self):
        """Updates or timestamps the attribute "update_at" with the current datetime."""
        self.update_at = datetime.now()
        model.storage.save()

    def __str__(self):
        """Return the string representation of the BaseModel instance for printing."""


    def to_dict(self):
        """Return a dictionary representing the BaseModel instance.

        Including the key/value pair "__class__"
        indicating the object's class name.
        """



