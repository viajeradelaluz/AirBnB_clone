#!/usr/bin/python3
""" Command interpreter to manage the AirBnB objects.
    """


from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import cmd
import json
import shlex

classes = ["BaseModel", "User", "State", "City",
           "Amenity", "Place", "Review"]

json_file = "file.json"


class HBNBCommand(cmd.Cmd):
    """ Contains the entry point of the command interpreter.
        """
    prompt = "(hbnb) "

    def do_create(self, line):
        """ Creates a new instance of BaseModel.
            """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        instance = eval(args[0])()
        instance.save()
        print(instance.id)

    def do_show(self, line):
        """ Prints a representation of an instance.
            """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return

        file_dict = storage.all()
        key_to_search = "{}.{}".format(args[0], args[1])
        if key_to_search in file_dict.keys():
            print(file_dict[key_to_search])
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """ Deletes an instance.
            """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        file_dict = storage.all()
        key_to_search = "{}.{}".format(args[0], args[1])
        if key_to_search in file_dict.keys():
            file_dict.pop(key_to_search)
            storage.save()
        else:
            print("** no instance found **")
            return

    def do_all(self, line):
        """ Prints all string representation of all instances.
            """
        args = line.split()
        file_dict = storage.all()
        if len(args) == 0:
            to_print = list()
            for key, value in file_dict.items():
                to_print.append(value.__str__())
            print(to_print)
            return
        if len(args) > 0 and args[0] not in classes:
            print("** class doesn't exist **")
            return
        if args[0] in classes:
            to_print = list()
            for key, value in file_dict.items():
                if args[0] == value.to_dict()["__class__"]:
                    to_print.append(value.__str__())
            print(to_print)
            return

    def do_update(self, line):
        """ Updates an instance based on the class name and id.
            """
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        file_dict = storage.all()
        key_to_search = "{}.{}".format(args[0], args[1])

        if key_to_search in file_dict.keys():
            if len(args) == 2:
                print("** attribute name missing **")
                return
            if len(args) == 3:
                print("** value missing **")
                return
            instance = file_dict[key_to_search]
            setattr(instance, args[2], args[3])
            storage.save()
        else:
            print("** no instance found **")
            return

    def emptyline(self):
        """ Empty line to not execute anything.
            """
        pass

    def do_quit(self, line):
        """ Quit command to exit the program.
            """
        return True

    def do_EOF(self, line):
        """ EOF command to exit the program.
            """
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
