#!/usr/bin/python3
"""Command interpreter for the AirBnB clone project"""

import cmd
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = "(hbnb) "

    def emptyline(self):
        """Called when an empty line is entered"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the programm"""
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()