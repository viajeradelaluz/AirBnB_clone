#!/usr/bin/python3
""" Command interpreter to manage the AirBnB objects.
    """


from models.base_model import BaseModel
from models import storage
import cmd
import json

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
        except:
            return
        key_to_search = "{}.{}".format(args[0], args[1])
        if key_to_search in file_dict.keys():
            instance = eval(args[0])(file_dict[key_to_search])
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
        except:
            return

    def do_all(self, line):
        """ Prints all string representation of all instances.
            """
        args = line.split()

        if args[1] not in classes:
            print("** class doesn't exist **")
            return
        #### To complete ###

    def do_update(self, line):
        """ Updates an instance based on the class name and id.
            """
        pass

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
