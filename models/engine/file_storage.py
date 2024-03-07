#!/usr/bin/python3
"""FileStorage class for serialize and deserialize objects"""

import json
from models.base_model import BaseModel
from datetime import datetime
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Manage serialization/deserialization of objects to/from json"""

    # path to the JSON file and dictionary to store object
    __file_path = "file.json"
    __objects = {}
    class_dict = {"BaseModel": BaseModel, "User": User, "Place": Place,
                  "Amenity": Amenity, "City": City, "Review": Review,
                  "State": State}

    def all(self, cls=None):
        """return the dictionary object or filtered by cls"""
        if cls is not None:
            return {
                key: obj
                for key, obj in self.__objects.items() if isinstance(
                    obj, cls)
            }
        return self.__objects

    def new(self, obj):
        """Add to the dictionary __objects the obj in format class name.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj
        self.save()

    def save(self):
        """serialize __objects to the JSON file"""
        obj_dict = {}
        for key, value in FileStorage.__objects.items():
            obj_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """deserialize the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.rsplit('.', 1)
                    value['created_at'] = datetime.strptime(
                        value['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
                    value['updated_at'] = datetime.strptime(
                        value['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
                    # convert value in strins
                    for k, v in value.items():
                        if isinstance(v, datetime):
                            value[k] = v.isoformat()

                    obj_class = globals()[class_name]
                    obj_instance = obj_class(**value)
                    self.__objects[key] = obj_instance
        except FileNotFoundError:
            pass
