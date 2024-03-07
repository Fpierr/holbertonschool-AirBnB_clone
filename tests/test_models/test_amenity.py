#!/usr/bin/python3

import unittest
import os
import pep8
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Class for testing Amenity"""

    @classmethod
    def setUpClass(cls):
        """Set up"""
        cls.amenity1 = Amenity()
        cls.amenity1.name = "Hot Tub"

    @classmethod
    def tearDownClass(cls):
        """Tear down class"""
        del cls.amenity1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_pep8_style(self):
        """Test PEP8 style"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0, "Fix PEP8")

    def test_amenity_is_subclass_of_base_model(self):
        """Test if Amenity is a subclass of BaseModel"""
        self.assertIsInstance(self.amenity1, BaseModel)

    def test_docstring_present(self):
        """Test if docstring is present"""
        self.assertIsNotNone(Amenity.__doc__)

    def test_attributes_exist(self):
        """Test if attributes exist"""
        self.assertIn('id', self.amenity1.__dict__)
        self.assertIn('created_at', self.amenity1.__dict__)
        self.assertIn('updated_at', self.amenity1.__dict__)
        self.assertIn('name', self.amenity1.__dict__)

    def test_attribute_type(self):
        """Test if attribute is of correct type"""
        self.assertIsInstance(self.amenity1.name, str)

    def test_save_updates_timestamps(self):
        """Test if save updates timestamps"""
        before_save = self.amenity1.updated_at
        self.amenity1.save()
        after_save = self.amenity1.updated_at
        self.assertNotEqual(before_save, after_save)

    def test_to_dict_method_exists(self):
        """Test if to_dict method exists"""
        self.assertTrue(hasattr(self.amenity1, 'to_dict'))


if __name__ == "__main__":
    unittest.main()
