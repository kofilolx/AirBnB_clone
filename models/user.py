#!/usr/bin/python3
"""Defines the User class"""
from models.base_model import BaseModel


class User(BaseException):
    """Represents a user entity.

    Attributes:
        email (str): The email address associated with the user.
        password (str): The password used for authentication.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
