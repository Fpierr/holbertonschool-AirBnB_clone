#!/usr/bin/python3
"""BaseModel class that defines common attributes/methods for other classes"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """Define all command and attributes for other classes"""

    def __init__(self, *args, **kwargs):
        """Define consctructor"""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.fromisoformat(value)
                if key != '__class__':
                    setattr(self, key, value)

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Return the string representation of BaseModel."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """update the instanse update attribute and call save on storage"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Create a dictionary that content the values of the instance"""
        model_dict = self.__dict__.copy()
        model_dict['__class__'] = self.__class__.__name__
        model_dict['created_at'] = self.created_at.isoformat()
        model_dict['updated_at'] = self.updated_at.isoformat()
        return model_dict
