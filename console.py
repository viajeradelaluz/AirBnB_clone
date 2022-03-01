#!/usr/bin/python3
""" Command interpreter to manage the AirBnB objects.
    """

import cmd


class HBNBCommand(cmd.Cmd):
    """ Contains the entry point of the command interpreter. """

    def __init__(self):
        """ Initialize the command interpreter.
            """
        super().__init__()
        self.prompt = "(hbnb) "

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
