#!/usr/bin/python3
"""Unittest for BaseModel class"""

import unittest
import os
import pep8
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test class for BaseModel"""

    @classmethod
    def setUpClass(cls):
        """Set up class: create an instance of BaseModel for testing"""
        cls.model = BaseModel()
        cls.model.name = "Fanuel"
        cls.model.my_number = 89

    @classmethod
    def tearDownClass(cls):
        """Tear down class: clean up resources after all tests"""
        del cls.model
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style_check(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_functions(self):
        """Test if certain functions are present in the class"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_attributes(self):
        """Test if the class has certain attributes"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_init(self):
        """Test the __init__ method"""
        self.assertTrue(isinstance(self.model, BaseModel))

    def test_save(self):
        """Test the save method"""
        self.model.save()
        self.assertNotEqual(self.model.created_at, self.model.updated_at)

    def test_to_dict(self):
        """Test the to_dict method"""
        model_dict = self.model.to_dict()
        self.assertEqual(self.model.__class__.__name__, 'BaseModel')
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
