#!/usr/bin/python3

import unittest
import os
import pep8
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up a State instance for testing."""
        cls.state1 = State()
        cls.state1.name = "North_Carolina_AKA_THE_BEST_STATE"

    @classmethod
    def tearDownClass(cls):
        """Clean up after testing."""
        del cls.state1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style_check(self):
        """
        Tests pep8 style.
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/state.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_is_subclass(self):
        """Check if State is a subclass of BaseModel."""
        self.assertTrue(issubclass(self.state1.__class__, BaseModel), True)

    def test_checking_for_functions(self):
        """Check if __doc__ is not None."""
        self.assertIsNotNone(State.__doc__)

    def test_has_attributes(self):
        """Check if State instance has certain attributes."""
        self.assertTrue('id' in self.state1.__dict__)
        self.assertTrue('created_at' in self.state1.__dict__)
        self.assertTrue('updated_at' in self.state1.__dict__)
        self.assertTrue('name' in self.state1.__dict__)

    def test_attributes_are_strings(self):
        """Check if name attribute is of type string."""
        self.assertEqual(type(self.state1.name), str)

    def test_save(self):
        """Test the save method."""
        self.state1.save()
        self.assertNotEqual(self.state1.created_at, self.state1.updated_at)

    def test_to_dict(self):
        """Test the to_dict method."""
        self.assertEqual('to_dict' in dir(self.state1), True)


if __name__ == "__main__":
    unittest.main()
