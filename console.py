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
           and print"""
        if len(com) == 0:
            print("** class name missing **")
            return
        new_class = None
        if (com):
            com_list = com.split()
            if len(com_list) == 1:
                if com in self.dictionary.keys():
                    new = self.dictionary[com]()
                    new_class.save()
                    print(new_class.id)
                else:
                    print("** class doesn't exist **")

    def show_com(self, com):
        """Prints the string representation of an instance based
           on the class name and id"""

        if len(com) == 0:
            print("** class name missing **")
            return
        elif com.split()[0] not in self.dictionary:
            print("** class doesn't exist **")
            return
        elif len(com.split()) > 1:
            i = com.split()[0] + "." + com.split()[1]
            if i in storage.all():
                i = storage.all()
                print(i[key])
            else:
                print("** no instance found **")
        else:
            print("** instance id missing **")

    def destroy_com(self, com):
        """Deletes an instance based on that class name and id"""

        if len(com) == 0:
            print("** class name missing **")
            return
        com_list = com.split()
        try:
            class_name = eval(com_list[0])
        except Exception:
            print("** class doesn't exist **")
            return
        if len(com_list) == 1:
            print('** instance id missing **')
            return
        if len(com_list) > 1:
            i = com_list[0] + "." + com_list[1]
            if i in storage.all():
                storage.all().pop(i)
                storage.save()
            else:
                print("** no instance found **")
                return

    def all_com(self, com):
        """Prints all string representations of all instances based or
           not on the class ex name"""

        if len(com) == 0:
            print([str(i) for i in storage.all().values()])
        elif com not in self.dictionary:
            print("** class doesn't exist **")
        else:
            print([str(i) for j, i in storage.all().items() if com in j])

    def update_com(self, com):
        """Updates an instance based on the class nameand id by adding or
           updating attribute"""
        com = com.split()
        if len(com) == 0:
            print("** class name missing **")
            return
        elif com[0] not in self.dictionary:
            print("** class doesn't exist **")
            return
        elif len(com) == 1:
            print("** instance id missing **")
            return
        else:
            i = com[0] + "." + com[1]
            if i in storage.all():
                if len(com) > 2:
                    if len(com) == 3:
                        print("** value missing **")
                    else:
                        setattr(
                            storage.all()[i],
                            com[2],
                            com[3][1:-1])
                        storage.all()[i].save()
                else:
                    print("** attribute name missing **")
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
