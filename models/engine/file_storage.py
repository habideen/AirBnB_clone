#!/usr/bin/python3
""" module containing the FileStorage class """


import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os

class FileStorage():
    """ class for file storage """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return the __object dictionary """

        return  self.__objects
    
    def new(self, obj):
        """ new update on the __objects every time an object created """
        ob_key = type(obj).__name__ + "." + obj.id
        self.__objects[ob_key] = obj

    def save(self):
        """ serialization """
        with open(self.__file_path, "w", encoding="utf-8") as jf:
            d = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(d, jf)

    def reload(self):
        """ deserialization """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as jf:
                for key, obj in json.loads(jf.read()).items():
                    obj = eval(obj['__class__'])(**obj)
                    self.__objects[key] = obj
