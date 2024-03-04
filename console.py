#!/usr/bin/python3
"""Command interpreter for the AirBnB clone project"""

import cmd
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        quit()

    def do_EOF(self, arg):
        """EOF command to exit the programm"""
        print()
        quit()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
