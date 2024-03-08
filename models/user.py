#!/usr/bin/python3
"""user class"""

from datetime import datetime
from models.base_model import BaseModel
import email


class User(BaseModel):
    '''base model class'''

    email = ""
    password = ""
    first_name = ""
    last_name = ""
