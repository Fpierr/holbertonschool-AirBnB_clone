#!/usr/bin/python3
"""FileStorage class for serialize and deserialize objects"""

import json
from models.base_model import BaseModel
from datetime import datetime
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Manage serialization/deserialization of objects to/from json"""

    # path to the JSON file and dictionary to store object
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return the dictionary object"""
        return self.__objects

    def new(self, obj):
        """Add to the dictionary __objects the obj in format class name.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serialize __objects to the JSON file"""
        obj_dict = {}
        for key, value in self.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """deserialize the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    value['created_at'] = datetime.strptime(
                        value['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
                    value['updated_at'] = datetime.strptime(
                        value['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
                    obj_class = globals()[class_name]
                    obj_instance = obj_class(**value)
                    self.__objects[key] = obj_instance
        except FileNotFoundError:
            pass
