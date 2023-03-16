#!/usr/bin/python3
""" Module containing the User Class """
from models.base_model import BaseModel


class User(BaseModel):
    """Class for a user object"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
