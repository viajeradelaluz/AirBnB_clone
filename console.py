#!/usr/bin/python3

import cmd


class HBNBCommand(cmd.Cmd):
    """ _summary_ """

    def __init__(self):
        """ _summary_ """
        super().__init__()
        self.prompt = "(hbnb) "

    def do_quit(self, line):
        """ _summary_ """
        exit()
        pass

    def do_EOF(self, line):
        """ _summary_ """
        exit()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
