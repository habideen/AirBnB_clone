#!/usr/bin/python3
""" module containing the parent class """


import uuid
import models
from datetime import datetime


class BaseModel():
    """ baseModel class """

    def __init__(self, *args, **kwargs):
        """ initializing  the class """

        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    dt = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, dt)
                    continue
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ return string rep. of the class"""

        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """ updating the public instance attr. update_at """

        self.update_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ return dictionery rep of  the keys and values of the instances """

        dict = self.__dict__.copy()
        dict["__class__"] = type(self).__name__
        dict["created_at"] = dict["created_at"].isoformat()
        dict["updated_at"] = dict["updated_at"].isoformat()
        return dict
