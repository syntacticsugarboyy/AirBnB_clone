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

    def do_quit(self, com):
        """This command intpreter should exit program"""
        return True

    def do_EOF(self, com):
        """This command interpreter should also exit program"""
        print("")
        return True

    def emptyline(self):
        """This should not execute anything"""
        pass

    def create_com(self, com):
        """Creates a new instance of basemodel, saves it to json file
           and prints id"""

    def destroy_com(self, com):
        """Deletes an instance based on that class name and id"""

    def all_com(self, com):
        """Prints all string representations of all instances based or
           not on the class ex name"""

    def update_com(self, com):
        """Updates an instance based on the class nameand id by adding or
           updating attribute"""


if __name__ == '__main__':
    HBNBCommand().cmdloop()
