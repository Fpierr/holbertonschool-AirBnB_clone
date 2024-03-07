#!/usr/bin/python3
"""
Entry to command interpreter
"""
import cmd
from models import storage
import models
from models.base_model import BaseModel


def parse(arg):
    """Helper method to parse user-typed input"""
    return tuple(arg.split())


class HBNBCommand(cmd.Cmd):
    """
    Entry to command interpreter
    """
    prompt = "(hbnb) "
    classes = {"BaseModel"}

    def do_EOF(self, arg):
        """Exit on Ctrl-D"""
        print()
        return True

    def do_quit(self, arg):
        """Exit on quit"""
        return True

    def emptyline(self):
        """Overwrite default behavior to repeat last cmd"""
        pass

    def do_create(self, arg):
        """Create instance specified by user"""
        if len(arg) == 0:
            print("** class name missing **")
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            args = parse(arg)
            instance = getattr(models, args[0])()
            instance.save()
            print(instance.id)

    def do_show(self, arg):
        """Print string representation: name and id"""
        if len(arg) == 0:
            print("** class name missing **")
            return
        args = parse(arg)
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        try:
            if args[1]:
                name = "{}.{}".format(args[0], args[1])
                if name not in storage.all().keys():
                    print("** no instance found **")
                else:
                    print(storage.all()[name])
        except IndexError:
            print("** instance id missing **")

    def do_destroy(self, arg):
        """Destroy instance specified by user; Save changes to JSON file"""
        if len(arg) == 0:
            print("** class name missing **")
            return
        args = parse(arg)
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        try:
            if args[1]:
                name = "{}.{}".format(args[0], args[1])
                if name not in storage.all().keys():
                    print("** no instance found **")
                else:
                    del storage.all()[name]
                    storage.save()
        except IndexError:
            print("** instance id missing **")

    def do_all(self, arg):
        """Print all objects or all objects of specified class"""
        args = parse(arg)
        obj_list = []
        if len(arg) == 0:
            for objs in storage.all().values():
                obj_list.append(objs)
            print(obj_list)
        elif args[0] in HBNBCommand.classes:
            for key, objs in storage.all().items():
                if args[0] in key:
                    obj_list.append(objs)
            print(obj_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Update if given exact object, exact attribute"""
        args = parse(arg)
        if len(args) >= 4:
            key = "{}.{}".format(args[0], args[1])
            cast = type(eval(args[3]))
            arg3 = args[3]
            arg3 = arg3.strip('"')
            arg3 = arg3.strip("'")
            setattr(storage.all()[key], args[2], cast(arg3))
            storage.all()[key].save()
        elif len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif ("{}.{}".format(args[0], args[1])) not in storage.all().keys():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        else:
            print("** value missing **")

    def do_count(self, arg):
        """Display count of instances specified"""
        if arg in HBNBCommand.classes:
            count = 0
            for key, objs in storage.all().items():
                if arg in key:
                    count += 1
            print(count)
        else:
            print("** class doesn't exist **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
