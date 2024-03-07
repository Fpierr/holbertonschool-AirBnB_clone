#!/usr/bin/python3
"""
Unittest to test FileStorage class
"""
import unittest
import pep8
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    '''Testing FileStorage'''

    @classmethod
    def setUpClass(cls):
        """Set up an instance of Review for testing"""
        cls.rev1 = Review()
        cls.rev1.place_id = "Raleigh"
        cls.rev1.user_id = "Greg"
        cls.rev1.text = "Grade A"

    @classmethod
    def tearDownClass(cls):
        """Tear down the instance of Review after testing"""
        del cls.rev1

    def tearDown(self):
        """Remove file.json if it exists after each test"""
        try:
            os.remove("file.json")
        except:
            pass

    def test_style_check(self):
        """
        Tests pep8 style
        """
        # Perform pep8 style check for the file_storage module
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_all(self):
        """
        Tests method: all (returns dictionary <class>.<id> : <obj instance>)
        """

        # Create an instance of FileStorage
        storage = FileStorage()

        # Retrieve the dictionary of objects
        instances_dic = storage.all()

        # Ensure the dictionary is not None, has the correct type, and is the same as __objects
        self.assertIsNotNone(instances_dic)
        self.assertEqual(type(instances_dic), dict)
        self.assertIs(instances_dic, storage._FileStorage__objects)

    def test_new(self):
        """
        Tests method: new (saves a new object into dictionary)
        """

        # Create an instance of FileStorage
        m_storage = FileStorage()

        # Retrieve the dictionary of objects
        instances_dic = m_storage.all()

        # Create a new User object
        melissa = User()
        melissa.id = 999999
        melissa.name = "Melissa"

        # Save the new object into the dictionary
        m_storage.new(melissa)

        # Create the key for the dictionary
        key = melissa.__class__.__name__ + "." + str(melissa.id)

        # Ensure the key exists in the dictionary
        self.assertIsNotNone(instances_dic[key])

    def test_reload(self):
        """
        Tests method: reload (reloads objects from string file)
        """

        # Create an instance of FileStorage
        a_storage = FileStorage()

        # Remove file.json if it exists
        try:
            os.remove("file.json")
        except:
            pass

        # Create an empty file.json
        with open("file.json", "w") as f:
            f.write("{}")

        # Open file.json and ensure it's empty
        with open("file.json", "r") as r:
            for line in r:
                self.assertEqual(line, "{}")

        # Reload the objects from file.json
        self.assertIs(a_storage.reload(), None)
