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
                if key == '__class__':
                    continue
                elif key in ['created_at', 'updated_at']:
                    try:
                        date_value = datetime.fromisoformat(value)
                    except ValueError:
                        raise ValueError(
                            "Invalid date format for {}: {}".format(
                                key, value))
                    setattr(self, key, date_value)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Return the string representation of BaseModel."""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """update the instanse update attribute and call save on storage"""
        self.updated_at = datetime.now()
        try:
            models.storage.new(self)
            models.storage.save()
        except Exception as e:
            print("Error saving instance: {}".format(e))
            raise

    def to_dict(self):
        """Create a dictionary that contains the values of the instance"""
        model_dict = {'__class__': type(self).__name__}

        for key, value in self.__dict__.items():
            if key in ['created_at', 'updated_at']:
                if hasattr(value, 'isoformat'):
                    model_dict[key] = value.isoformat()
                else:
                    model_dict[key] = value
            else:
                model_dict[key] = value
        return model_dict
