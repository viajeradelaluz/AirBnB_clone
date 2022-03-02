#!/usr/bin/python3
""" Command interpreter to manage the AirBnB objects.
    """

import cmd

classes = ["BaseModel", "User", "State", "City",
               "Amenity", "Place", "Review"]

class HBNBCommand(cmd.Cmd):
    """ Contains the entry point of the command interpreter. """

    
    def __init__(self):
        """ Initialize the command interpreter.
            """
        super().__init__()
        self.prompt = "(hbnb) "


    def do_create(self, line):
        """ Creates a new instance of BaseModel.
            """
        args = line.split()

        if args[1] == "":
            print("** class name missing **")
            return

        if args[1] not in classes:
            print("** class doesn't exist **")
            return

        instance = eval(args[1])()
        instance.save()
        print(instance.id)


    def do_show(self, line):
        """ Prints a representation of an instance.
            """
        args = line.split()

        if args[1] == "":
            print("** class name missing **")
            return

        if args[1] not in classes:
            print("** class doesn't exist **")
            return

        if not args[2]:
            print("** instance id missing **")
            return

        ##########################
        # To complete final task #
        print("** no instance found **")
        ##########################


    def do_destroy(self, line):
        """ Deletes an instance.
            """
        args = line.split()

        if args[1] == "":
            print("** class name missing **")
            return

        if args[1] not in classes:
            print("** class doesn't exist **")
            return

        if not args[2]:
            print("** instance id missing **")
            return

        ##########################
        # To complete final task #
        print("** no instance found **")
        ##########################


    def do_all(self, line):
        """ Prints all string representation of all instances.
            """
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
