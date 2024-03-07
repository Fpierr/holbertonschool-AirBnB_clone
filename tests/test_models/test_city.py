#!/usr/bin/python3

import unittest
import os
import pep8
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up a City instance for testing"""
        cls.city1 = City()
        cls.city1.name = "Raleigh"
        cls.city1.state_id = "NC"

    @classmethod
    def tearDownClass(cls):
        """Clean up resources after testing"""
        del cls.city1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style_check(self):
        """Check PEP8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/city.py'])
        self.assertEqual(p.total_errors, 0, "Fix PEP8")

    def test_is_subclass(self):
        """Test if City is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.city1.__class__, BaseModel), True)

    def test_checking_for_functions(self):
        """Check if docstring is present"""
        self.assertIsNotNone(City.__doc__)

    def test_has_attributes(self):
        """Test if City instance has required attributes"""
        self.assertTrue('id' in self.city1.__dict__)
        self.assertTrue('created_at' in self.city1.__dict__)
        self.assertTrue('updated_at' in self.city1.__dict__)
        self.assertTrue('state_id' in self.city1.__dict__)
        self.assertTrue('name' in self.city1.__dict__)

    def test_attributes_are_strings(self):
        """Test if specific attributes are of string type"""
        self.assertEqual(type(self.city1.name), str)
        self.assertEqual(type(self.city1.state_id), str)

    def test_save(self):
        """Test if save updates timestamps"""
        self.city1.save()
        self.assertNotEqual(self.city1.created_at, self.city1.updated_at)

    def test_to_dict(self):
        """Test if to_dict method exists"""
        self.assertEqual('to_dict' in dir(self.city1), True)


if __name__ == "__main__":
    unittest.main()
