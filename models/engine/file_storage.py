#!/usr/bin/python3
"""
recreate a BaseModel from another one by using a dictionary representation
"""
from xml.etree.ElementTree import TreeBuilder
from models.base_model import BaseModel
from models.review import Review
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.user import User
from models.state import State
import json
import os


class FileStorage:
    __file_path = 'file.json'
    __objects = {}
    class_dict = {
        'BaseModel': BaseModel,
        'Review': Review,
        'Amenity': Amenity,
        'City': City,
        'Place': Place,
        'User': User,
        'State': State
    }

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key"""
        if obj:
            FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """serializes __objects to the JSON file """
        new_dict = {}
        for keys, values in FileStorage.__objects.items():
            new_dict[keys] = values.to_dict()

        with open(FileStorage.__file_path, 'w') as file:
            json.dump(new_dict, file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                new_obj = json.load(f)
            for key, val in new_obj.items():
                obj = self.class_dict[val['__class__']](**val)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass
