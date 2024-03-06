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
                if key in ['created_at', 'updated_at']:
                    if isinstance(value, str):
                        value = datetime.fromisoformat(value)
                    setattr(self, key, value)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Return the string representation of BaseModel."""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, str(self.__dict__))

    def save(self):
        """update the instanse update attribute and call save on storage"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Create a dictionary that contains the values of the instance"""
        model_dict = self.__dict__.copy()

        for key in ['created_at', 'updated_at']:
            if key in model_dict and hasattr(model_dict[key], 'isoformat'):
                model_dict[key] = model_dict[key].isoformat()

        model_dict['__class__'] = type(self).__name__
        return model_dict
