#!/usr/bin/python3

"""A program that contains the entry point of the command interpreter
"""

import cmd
from models.base_model import BaseModel
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models.user import User
import models


class HBNBCommand(cmd.Cmd):
    """This defines the command interpreter"""
    prompt = "(hbnb)"
    dictionary = {"BaseModel": BaseModel, "Place": Place, "City": City,
                  "Amenity": Amenity, "State": State, "Review": Review,
                  "User": User}

    def do_quit(self, arg):
        """This command intpreter should exit program"""
        return True

    def do_EOF(self, arg):
        """This command interpreter should also exit program"""
        print("")
        return True

    def emptyline(self):
        """This should not execute anything"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
