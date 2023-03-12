#!/usr/bin/python3
"""Main console modul
This system is used for database CRUD
Using static web pages
"""

import cmd

class AirBNBCommand(cmd.Cmd):
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


if __name__ == "__main__":
    AirBNBCommand().cmdloop()
