#!/usr/bin/python3
""" Command interpreter to manage the AirBnB objects.
    """


from models.base_model import BaseModel
from models import storage
import cmd
import json
import shlex

classes = ["BaseModel", "User", "State", "City",
           "Amenity", "Place", "Review"]

json_file = "file.json"


class HBNBCommand(cmd.Cmd):
    """ Contains the entry point of the command interpreter.
        """

    def __init__(self):
        """ Initialize the command interpreter.
            """
        super().__init__()
        self.prompt = "(hbnb) "

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
        try:
            with open(json_file) as file:
                file_dict = json.load(file)
        except Exception:
            return
        key_to_search = "{}.{}".format(args[0], args[1])
        if key_to_search in file_dict.keys():
            instance = eval(args[0])(**file_dict[key_to_search])
            print(instance)
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
        key_to_search = "{}.{}".format(args[0], args[1])
        try:
            with open(json_file) as file:
                file_dict = json.load(file)
                if key_to_search in file_dict.keys():
                    file_dict.pop(key_to_search)
                else:
                    print("** no instance found **")
                    return
            with open(json_file, mode='w') as file:
                json.dump(file_dict, file)
        except Exception:
            return

    def do_all(self, line):
        """ Prints all string representation of all instances.
            """
        args = line.split()
        try:
            with open(json_file) as file:
                file_dict = json.load(file)
        except Exception:
            return
        if len(args) == 0:
            to_print = list()
            for key, value in file_dict.items():
                instance = eval(value["__class__"])(**value)
                to_print.append(instance.__str__())
            print(to_print)
            return
        if len(args) > 0 and args[0] not in classes:
            print("** class doesn't exist **")
            return
        if args[0] in classes:
            to_print = list()
            for key, value in file_dict.items():
                if args[0] == value["__class__"]:
                    instance = eval(args[0])(**value)
                    to_print.append(instance.__str__())
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
        key_to_search = "{}.{}".format(args[0], args[1])
        try:
            with open(json_file) as file:
                file_dict = json.load(file)
                if key_to_search in file_dict.keys():
                    if len(args) == 2:
                        print("** attribute name missing **")
                        return
                    if len(args) == 3:
                        print("** value missing **")
                        return
                    instance = eval(args[0])(**file_dict[key_to_search])
                    setattr(instance, args[2], args[3])
                    file_dict[key_to_search] = instance.to_dict()
                else:
                    print("** no instance found **")
                    return
            with open(json_file, mode='w') as file:
                json.dump(file_dict, file)
        except Exception:
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
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
