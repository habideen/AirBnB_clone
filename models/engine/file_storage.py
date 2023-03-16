#!/usr/bin/python3
""" module  containining the FileStorage class """
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """ this is the file storage class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects."""
        return (self.__objects)

    def new(self, obj):
        """ update objects dictionary everytime
        a new object is created"""
        obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[obj_key] = obj

    def save(self):
        """method that serialize object files in to json file"""
        with open(self.__file_path, 'w', encoding="utf-8") as fp:
            jdict_ = {}
            for k, v in self.__objects.items():
                dict_ = self.__objects[k].to_dict()
                jdict_[k] = dict_
            fp.write(json.dumps(jdict_))

    def reload(self):
        """a method that deserialize JSON files"""
        dict_ = {}
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding="utf-8") as fp:
                str_ = fp.read()
                dict_ = json.loads(str_)
                for k, v in dict_.items():
                    class_ = v['__class__']
                    create_class = valid_classes[class_]
                    self.__objects[k] = create_class(**v)
