#!/usr/bin/python3
""" module containing the City Class """


from models.base_model import BaseModel


class City(BaseModel):
    """Class for  City objects/models"""

    state_id = ""
    name = ""
