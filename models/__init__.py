#!/usr/bin/python3
"""Init module for the models package"""

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

# Dictionary to store all classes
classes = {"BaseModel": BaseModel}

# Create an instance of FileSorage
storage = FileStorage()
storage.reload()
