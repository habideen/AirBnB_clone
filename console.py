#!/usr/bin/python3
"""Main console modul
This system is used for database CRUD
Using static web pages
"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage
import models
import json


class HBNBCommand(cmd.Cmd):
    """Command processor base class"""
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """End of Line to exit program"""
        return True

    def do_quit(self, line):
        """Quit command to exit program"""
        return True

    def emptyline(self):
        """The last command won't be repeated if an empty line is pass"""
        pass

    def do_create(self, cls):
        """Creates a new class instance and save it to  JSON file and print>"""
        if cls == "":
            print("** class name missing **")
        elif cls not in HBNBCommand.class_list:
            print("** class doesn't exist **")
        else:
            print((eval(cls)()).id)
            storage.save()
    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id"""
        args_arr = split(arg.strip(), posix=False)

        if not arg:
            print('** class name missing **')
        elif args_arr[0] not in HBNBCommand.__valid_classes:
            print('** class doesn\'t exist **')
        elif len(args_arr) == 1:
            print('** instance id missing **')
        else:
            key = "{}.{}".format(args_arr[0], args_arr[1].replace('"', ''))
            if key not in storage.all():
                print('** no instance found **')
            else:
                print(storage.all()[key])

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id """
        args_arr = split(arg.strip(), posix=False)

        if not arg:
            print('** class name missing **')
        elif args_arr[0] not in HBNBCommand.__valid_classes:
            print('** class doesn\'t exist **')
        elif len(args_arr) == 1:
            print('** instance id missing **')
        else:
            key = "{}.{}".format(args_arr[0], args_arr[1])
            if key not in storage.all():
                print('** no instance found **')
            else:
                storage.all().pop(key)
                storage.save()

    def do_all(self, arg):
        """ Prints all string representation of all instances """
        arg = arg.strip()
        objs_dict = storage.all()

        if arg and arg not in HBNBCommand.__valid_classes:
            print('** class doesn\'t exist **')
        else:
            objs_list = []
            for obj in objs_dict.values():
                if not arg:
                    objs_list.append(obj.__str__())
                elif type(obj).__name__ == arg:
                    objs_list.append(obj.__str__())
            print(objs_list)

    def __update_from_dict(self, dct):
        """Updates an instance based on the class name and id
        by adding or updating an attribute"""

        if not dct.get('class', False):
            print('** class name missing **')
        elif dct['class'] not in HBNBCommand.__valid_classes:
            print('** class doesn\'t exist **')
        elif not dct.get('id', False):
            print('** instance id missing **')
        else:
            key = "{}.{}".format(dct['class'], dct['id'])
            if key not in storage.all():
                print('** no instance found **')
            else:
                forbiden_update = ['id', 'created_at', 'updated_at', 'class']
                for attr, value in dct.items():
                    if attr not in forbiden_update:
                        obj = storage.all()[key]
                        if attr in obj.__dict__:
                            value = type(obj.__dict__[attr])(value)
                        obj.__setattr__(attr, value)
                        storage.save()

    def do_update(self, arg):
        """Updates an instance based on the class name
        and id """
        args_arr = split(arg.strip(), posix=False)

        if not arg:
            print('** class name missing **')
        elif args_arr[0] not in HBNBCommand.__valid_classes:
            print('** class doesn\'t exist **')
        elif len(args_arr) == 1:
            print('** instance id missing **')
        else:
            key = "{}.{}".format(args_arr[0], args_arr[1])
            if key not in storage.all():
                print('** no instance found **')
            elif len(args_arr) == 2:
                print('** attribute name missing **')
            elif len(args_arr) == 3:
                print('** value missing **')
            else:
                forbiden_update = ['id', 'created_at', 'updated_at']
                if args_arr[2] not in forbiden_update:
                    attr = args_arr[2].replace('"', '')
                    value = eval(args_arr[3])
                    obj = storage.all()[key]
                    if attr in obj.__dict__:
                        value = eval(type(obj.__dict__[attr]).__name__)(value)
                    obj.__setattr__(attr, value)
                    storage.save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()
