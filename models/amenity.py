#!/usr/bin/python3
"""Amenity module"""

from models.base_model import BaseModel
from datetime import datetime


class Amenity(BaseModel):
    """Amenity class"""
    name = ""
    updated_at = datetime.now()
