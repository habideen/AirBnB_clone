#!/usr/bin/python3
""" this module contains the base model class """


import models
import uuid
from datetime import datetime


class BaseModel():
    """ this is the baseModel class """
    def __init__(self, *args, **kwargs):
        """ initialization """
